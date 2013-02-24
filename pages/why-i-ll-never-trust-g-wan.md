title: "Why I'll never trust G-WAN"
date: 2012-10-30
tags: [vaporware]
abstract: A webserver that's 4 time faster than nginx? Monkey likes! But...

Today a link on Hacker News got my attention: [Node.js is just all hype](http://gwan.com/blog/20121027.html). Since I'm inclined to think the same, I started reading it. Imagine my disappointment when the article rapidly changed argument and started talking about G-WAN as the Cinderella of the "Next big things Club". Anyhow, the idea of having an application server that's not bound to the technology you want to use was interesting.

So I did what I always do when somebody is trying to sell me a new tecnology: I googled it for feedbacks and documentation.

Well, I found a couple of nice blog posts with benchmarks (a link for all: [http://nbonvin.wordpress.com/2011/03/14/apache-vs-nginx-vs-varnish-vs-gwan/](http://nbonvin.wordpress.com/2011/03/14/apache-vs-nginx-vs-varnish-vs-gwan/)) that gave credit to the G-WAN claim about speed. But what about serving something in Python? Or PHP? Surely the documentation will talk profusely about this kind of integration.

But... where the heck is the documentation? Maybe it's me, but not finding a big "Documentation" button on the official website felt strange.
Digging a little bit I found [a PDF](http://gwan.ch/archives/gwan_linux.pdf) named "Users manual".

After reading it this is what I think: that's not documentation, that's propaganda. Do you know what the PDF says about integration with [put your favourite technology here]?

<blockquote>
<strong>Extending G-WAN further (PHP, Java, C#, C++, Python, Perl, Js, etc.)</strong>
<br><br>
You don’t know, don’t like or don’t use ANSI C. Or you have a huge code-base in another language and you would like to use G-WAN with your favorite scripted or compiled language.
<br><br>
Good news: compiled languages can be used from G-WAN (see the C++ and Objective-C/C+ + examples).
<br><br>
If there's no compiler available, then you can use a C Servlet or an Handler (use the after_read state) to:
<br>
– redirect requests to another application server and then have G-WAN cache them,
<br>
– invoke compiled libraries (your compiled code invoked by your C script or Handler),
<br>
– call a script engine (via fastCGI, or anyo ther interface).
<br><br>
Here are G-WAN handler examples for popular scripted languages:
<br><br>
Javascript:
<br>
http://forum.gwan.com/index.php?p=/discussion/comment/3003/#Comment_3003
<br>
Lua:
<br>
http://forum.gwan.com/index.php?p=/discussion/comment/4061/#Comment_4061
<br>
Google Go:
<br>
http://forum.gwan.com/index.php?p=/discussion/comment/4044/#Comment_4044
<br>
Python:
<br>
http://forum.gwan.com/index.php?p=/discussion/comment/4126/#Comment_4126
<br><br>
As almost all other languages have been created in C (or, like Scala written in Java, have been created from a language written in C) you will not have trouble to interface C with whatever you need to use with C.
<br><br>
Just keep in mind that using external code will inevitably add overhead (slow-downs) and bugs to G-WAN.
<br><br>
The less you have layers of code, the safest (and fastest) your system will be. 
<br><br>
G-WAN was created for this sole reason.
</blockquote>

Really? Softwares have bugs? You don't say?

Of course, the links are broken and looks like there is not any kind of article/blog/news/howto/meme about how to integrate your software with G-WAN.

Add to this that the software is closed source and if you have problems you must pay for support and I have element enough to say: *stay away from it!*

