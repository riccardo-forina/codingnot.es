title: "https, http 2.0 and SPDY"
date: 2013-10-22
tags: [performance]
abstract: The future and the now

Today I was reading [Ilya Grigorik's presentation](https://docs.google.com/presentation/d/1eqae3OBCxwWswOsaWMAWRpqnmrVVrAfPQclfSqPkXrA/present#slide=id.p19) about HTTP 2.0.

It's amazing. I mean, you can stop worring about sprites and concatenation and _plus_ everything is faster?

<img src="//www.reactiongifs.com/wp-content/uploads/2012/11/take-my-money.gif" alt="Shut up and take my money">

Unfortunately, the due date is somewhere in 2014. Enter SPDY.

## SPDY

<blockquote cite="http://en.wikipedia.org/wiki/SPDY">
  SPDY (pronounced speedy) is an open networking protocol developed primarily at Google for transporting web content. (...) The goal of SPDY is to reduce web page load time.
</blockquote>

How does it works? Basically, SPDY will:

- compress request and response headers
- parellelize requests over a single connection
- push resources like CSS files and JS files to the client when possible and makes sense

Or, if you're like me, you can just think about black vodoo magic and be happy about that the result will be faster navigation for compatible clients (read Chrome, Firefox, Android browser. Not Safari, because who knows).

## I want it too! What do I need?

Not too much really, but some $/€/£/¥/whatever to gain access to a valid SSL certificate. Yes, because SPDY to work needs a web server with a working https configuration. Nope, a self-signed certificate doesn't work.

Then you need a SPDY-enabled web server.

### Apache
If you use Apache, you just have to install [mod_spdy](https://developers.google.com/speed/spdy/mod_spdy/) and you're done.

### nginx

If you use Nginx, you need at least version 1.4 that has built-in support for SPDY. If not you [have to patch your server](http://nginx.org/patches/spdy/README.txt).

### Redirect http traffic to the new https

Yes, because SPDY can't work for http connections, so you have to configure your webserver to redirect everything.

If you have social plugins on your site, remember that your page will have new urls. So, if you are like me and you didn't use some unique id instead of your url you will lose everything. Luckly enough, there are ways to limit damage, like [Disqus's Migration Tool](http://help.disqus.com/customer/portal/articles/286778-migration-tools).

    Yes, comments are all messed up right now (2013-10-22), I hope that the migration tool works like expected... :P

### Check if everything is working

Super easy, point your browser to [spdycheck.org](http://spdycheck.org/#riccardo.forina.me), write your domain and you'll get a complete sanity check of your SPDY setup!

If you want to get fancy, install an extension for your browser (SPDY indicator [for Chrome](https://chrome.google.com/webstore/detail/spdy-indicator/mpbpobfflnpcgagjijhmgnchggcjblin) and [for Firefox](https://addons.mozilla.org/it/firefox/addon/spdy-indicator/reviews/)) to be always updated about who is a member of the SPDY club.
