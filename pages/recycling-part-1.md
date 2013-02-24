title: "Recycling! (part 1): build your new website with Flask (and Twitter Bootstrap) and run it on Openshift"
date: 2012-07-31
tags: [howto, openshift, flask, bootstrap]
abstract: Are you a lazy developer but still want a website? And without spending a cent too? Me too! Let's see how after the jump.

So you want a website. Something yours, were you can mess around and experiment with something seen on Hacker News. That's fine, we share the same need.

What do we need?

* A web framework (something to handle urls, contents, templating, etc.) 
* An hosting solution. That's important, we want it compatible with our framework, easy to work with, and cheap.
* Do you really want to reinvent the html/css wheel _again_? Well, I don't, so we need some html framework. Mobile support is a plus.

## Web framework
A Google search for 'web framework' will give us about 246,000,000 results. Not bad.

Since I'm a pythonista, I'll focus on python based solutions.  
For a nice long list of python based web frameworks, you can refer to the official python wiki for a [full list](http://wiki.python.org/moin/WebFrameworks/).

For my daily work, I use Django. It's a really cool framework full of features with a lot of classy touches. I use it since verion 1.0 (the latest stable release is 1.4) and I consider myself quite expert with it.
  
That's why for this website I have chosen [Flask](http://flask.pocoo.org/). 

No, I'm not nuts. Django is great, but there's too much setup to bother with, and I want to see results _right now_.  Flask is a microframework with all the features I need: url dispatcher, templating system, documentation. You can start in minutes without worring about what you'll do in the future: refactoring is easy with Flask.
 
Oh, I don't want a database either (databases costs money). I want something easier, something based on [Markdown](http://daringfireball.net/projects/markdown/).  
Guess what? Flask [has an app](http://packages.python.org/Flask-FlatPages/) for that.

## Hosting
Plenty of choices here too. But we are python developers, we need something more than an (s)ftp where to drop some.php file, so what about some git support? And don't forget we want it cheap!

Impossibile?

Maybe, but at the moment of this writing Red Hat has a _free_ hosting solution for us greedy developers: [OpenShift](https://openshift.redhat.com/app/).

I can't personally tell you about the scalable part, but I can confirm how easy is to deploy something on it. Creating an account, an app (this website), adapt the code to it and going online has been a matter of 30 minutes.

## HTML/CSS framework
Again, too many options. I choose [Twitter Bootstrap](http://twitter.github.com/bootstrap/), because I'm using it at work and the responsive layout is a great plus on his side (try resizing the page or use your smartphone, qrcode [here](http://qr.kaywa.com/img.php?s=8&d=http%3A%2F%2Fnotes-riccardoforina.rhcloud.com%2Frecycling-part-1%2F)).

<strike>Yes, I know what you're telling. My website will look exactly like dozens. Maybe, but I'm a good person and will give you an [alternate version of this website](http://wonder-tonic.com/geocitiesizer/content.php?theme=3&music=3&url=codingnot.es) if you like it more :)</strike> Update: the website got a (dozen of) restyling, so the previous statement is not valid anymore.

## Put all together
Now we have all the pieces to build our new shining website! Trust me, it will be super easy.

But we'll do it next time, stay tuned!

Update: [the second part is online](/recycling-part-2/)