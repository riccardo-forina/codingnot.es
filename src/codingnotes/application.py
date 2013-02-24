import os
import sys
import re
import socket
import pytz
from urlparse import urljoin
from datetime import datetime, time
from flask import Flask, render_template, request, url_for, Response
from flask_assets import Environment
from flask_frozen import Freezer
from collections import defaultdict
from flask_flatpages import FlatPages
from werkzeug.contrib.atom import AtomFeed

utc = pytz.utc

HOSTNAME = socket.gethostname()
DEBUG = False
if '.local' in HOSTNAME:
    DEBUG = True

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
# LESS_BIN = os.path.join(SCRIPT_ROOT, '..', 'node_modules', 'less', 'bin', 'lessc')
LESS_LINE_NUMBERS = 'mediaquery'
FREEZER_DESTINATION = os.path.join(SITE_ROOT, '..', '..', 'build')
FLATPAGES_ROOT = os.path.join(SITE_ROOT, '..', '..', 'pages')

app = Flask(
    import_name='codingnotes',
    static_folder=os.path.join(SITE_ROOT, '..', '..', 'static'),
    template_folder=os.path.join(SITE_ROOT, '..', '..', 'templates'),
)

assets = Environment(app)
assets.manifest = False
assets.cache = False
if DEBUG:
    assets.manifest = False
    assets.cache = None
freezer = Freezer(app)
pages_on_disk = FlatPages(app)

app.config.from_object(__name__)


def is_published(post_date):
    return utc.localize(datetime.utcnow()) >= utc.localize(datetime.combine(post_date, time(0, 0, 0)))
published_pages = sorted([p for p in pages_on_disk if is_published(p.meta.get('date', '2099-12-31'))], key=lambda p: p.meta['date'])


def get_latest_pages(limit=10):
    pages = published_pages if not request.args.get('preview') else pages_on_disk
    # Articles are pages with a publication date
    articles = (p for p in pages if 'date' in p.meta)
    # Show the 10 most recent articles, most recent first.
    latest = sorted(articles, reverse=True,
                    key=lambda p: p.meta['date'])
    return latest[:limit]


def get_tags():
    pages = published_pages if not request.args.get('preview') else pages_on_disk

    tags = defaultdict(int)
    for page in pages:
        for tag in page.meta['tags']:
            tags[tag] += 1
    return tags


def make_external(url):
    return urljoin(request.url_root, url)


def feed(articles):
    articles = sorted(articles, reverse=True,
                    key=lambda p: p.meta['date'])
    feed = AtomFeed(
        'Coding notes by Riccardo Forina',
        feed_url=request.url,
        url=request.url_root,
        icon=make_external(url_for('static', filename="icons/favicon.ico")),
        logo=make_external(url_for('static', filename="icons/favicon.ico")),
    )
    for article in articles:
        feed.add(
            article.meta['title'],
            unicode(article.html),
            content_type='html',
            author='Riccardo Forina',
            url=make_external(url_for('page', path=article.path)),
            updated=article.meta.get('updated', article.meta['date']),
            published=article.meta['date'],
        )
    return feed.get_response()


@app.errorhandler(404)
def page_not_found(e):
    latest = get_latest_pages()
    return render_template('404.html', pages=latest), 404


@app.route('/')
def index():
    latest = get_latest_pages(limit=None)
    return render_template('index.html',
        pages=latest,
        tags=get_tags(),
        now=utc.localize(datetime.utcnow())
    )


@app.route('/tag/<string:tag>/recent.atom')
def tag_feed(tag):
    pages = published_pages if not request.args.get('preview') else pages_on_disk
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return feed(tagged)


@freezer.register_generator
def tag_feed_generator():
    for tag in get_tags():
        yield 'tag_feed', {'tag': tag}


@app.route('/tag/<string:tag>/')
def tag(tag):
    pages = published_pages if not request.args.get('preview') else pages_on_disk

    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html',
        pages=tagged,
        tag=tag,
        tags=get_tags(),
    )


@app.route('/<path:path>/')
def page(path):
    # pages = published_pages if not request.args.get('preview') else pages_on_disk

    page = pages_on_disk.get_or_404(path)
    index = published_pages.index(page)
    previous_page = published_pages[index - 1] if index > 0 else None
    next_page = published_pages[index + 1] if index < (len(published_pages) - 1) else None
    # print previous_page, next_page
    # if not page in pages:
    #     abort(404)
    return render_template('page.html',
        page=page,
        previous_page=previous_page,
        next_page=next_page,
        latest=get_latest_pages(5),
        tags=get_tags()
    )


@app.route('/status/')
def status():
    return render_template('status.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html',
        latest=get_latest_pages(5)
    )


@app.route('/recent.atom')
def site_feed():
    return feed(get_latest_pages())


@app.route('/robots.txt')
def robots():
    return render_template('robots.txt', sitemap_url=make_external(url_for('sitemap')))


@app.route('/sitemap.xml')
def sitemap():
    urls = [make_external(url_for('index')), make_external(url_for('status'))]
    urls += [make_external(url_for('page', path=article.path)) for article in published_pages]
    urls += [make_external(url_for('tag', tag=tag)) for tag in get_tags()]
    return Response(
        response=render_template('sitemap.xml', urls=urls), mimetype='app/xml')


def truncate_html_words(s, num):
    """
    Truncates html to a certain number of words (not counting tags and comments).
    Closes opened tags if they were correctly closed in the given html.
    """
    length = int(num)
    if length <= 0:
        return ''
    # Set up regular expressions
    re_whitespace = re.compile(r'\s+')
    re_html_comment = re.compile(r'<!--.*?-->', re.DOTALL)
    re_tag_singlet = re.compile(r'<[^>]+/>')
    re_tag = re.compile(r'<([^>/\s]+)[^>]*>')
    re_tag_close = re.compile(r'</([^>\s]+)[^>]*>')
    re_non_alphanumeric = re.compile(r'[^\w<]+')
    re_word = re.compile(r'[^<\s]+')
    # Set up everything else
    tags = []
    words = 0
    pos = 0
    len_s = len(s)
    elipsis_pos = 0
    elipsis_required = 0
    while pos < len_s:
        # Skip white space, comment, or singlet
        m = re_whitespace.match(s, pos) or re_html_comment.match(s, pos) or re_tag_singlet.match(s, pos)
        if m:
            pos = m.end(0)
            continue
        # Check for tag
        m = re_tag.match(s, pos)
        if m:
            pos = m.end(0)
            if not elipsis_pos:
                tag = m.group(1).lower()
                tags.append(tag)
            continue
        # Check for close tag
        m = re_tag_close.match(s, pos)
        if m:
            pos = m.end(0)
            if not elipsis_pos:
                tag = m.group(1).lower()
                try:
                    tags.remove(tag)
                except ValueError:
                    pass
            continue
        # Skip non-alphanumeric
        m = re_non_alphanumeric.match(s, pos)
        if m:
            pos = m.end(0)
            continue
        # Check for word
        m = re_word.match(s, pos)
        if m:
            pos = m.end(0)
            words += 1
            if words == length:
                elipsis_pos = pos
            if words > length:
                elipsis_required = 1
                break
            continue
        # Shouldn't ever actually get here
        break
    if elipsis_required:
        out = s[:elipsis_pos]
        if not out.endswith('...'):
            out += ' ...'
    else:
        out = s[:pos]
    # Look for closing tags for any tags still open
    tags.reverse()
    temppos = pos
    for tag in tags:
        while 1:
            m = re_tag_close.search(s, temppos)
            if m:
                temppos = m.end(0)
                if m.group(1) == tag:
                    out += m.group(0)
                    pos = temppos
                    break
            else:
                break
    return out


app.jinja_env.filters['truncate_html_words'] = truncate_html_words


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run('0.0.0.0')


if __name__ != '__main__':
    import newrelic.agent
    newrelic.agent.initialize(os.path.join(SITE_ROOT, 'newrelic.ini'))
