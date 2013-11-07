/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
var disqus_shortname = 'notesriccardoforina'; // required: replace example with your forum shortname
// var disqus_url = '';

function embedDisqusComments() {  
  var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
  dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
  (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
}

function embedDisqusCommentsCount() {
  var s = document.createElement('script'); s.async = true;
  s.type = 'text/javascript';
  s.src = '//' + disqus_shortname + '.disqus.com/count.js';
  (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
}

function loadCodePrettify() {
  var s = document.createElement('script'); s.async = true;
  s.type = 'text/javascript';
  s.src = '//google-code-prettify.googlecode.com/svn/loader/run_prettify.js?skin=desert';
  (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
}

(function($) {
  $(document).ready(function() {
    var qn = $('.quick-nav');
    $('article h2:not(.no-anchor)').each(function(idx) {
      var h2 = $(this),
          id = h2.text().toLowerCase()
                        .replace(/ /g,'-')
                        .replace(/[^\w-]+/g,'');
      h2.before('<span class="qna" id="' + id + '"><a href="#' + id + '"><i class="icon-tag-fill"></i></a></span>');
      qn.append('<li><a href="#' + id + '"><i class="icon-tag-fill"></i> ' + h2.text() + '</a></li>')
    });
    var titleHeight = $('h1').height();
    var body = $('body');

    $('#disqus_thread').waypoint(embedDisqusComments, {
      triggerOnce: true,
      offset: 'bottom-in-view'
    });

    if ($('pre').length > 0) {
      loadCodePrettify();
    }
    $(window).scroll(function() {
      if ($(window).scrollTop() > titleHeight) {
        body.addClass('scrolling');
      } else {
        body.removeClass('scrolling');
      }
    });
  });

  embedDisqusCommentsCount();

})(jQuery);