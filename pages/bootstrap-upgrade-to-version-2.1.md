title: "Bootstrap upgrade to version 2.1"
date: 2012-08-22
tags: [bootstrap]
abstract: The guys working on Twitter Bootstrap just released the new version 2.1. Codingnot.es has been upgraded to it and got a small restyling. Let's see what's changed!

Codingnot.es is mainly my own playground, so when I got the news that Twitter released a new version of Bootstrap I was eager to test it on it!

The greatest news of all is the new documentation. Frankly, the old website wasn't that clear on how to use the library, but now is way better. Not perfect, but better :)

Looks like the typeahead plugin got some async love. If you don't know it, I'm talking about [this plugin](http://twitter.github.com/bootstrap/javascript.html#typeahead). Since the previous version, typeahead could work only on static json data. Now the <code>source</code> option accepts a function so ajax retrieval should be viable.

There is a new plugin too, [Affix](http://twitter.github.com/bootstrap/javascript.html#affix). It's useful to fix a content to follow the scroll. You can see it working on the right column. An hint: remember to fix a width to the affixed element, the Bootstrap's grid will _not_ help you here :)

Dropdowns can now be nested. Let's hope it's not abused, too many nested dropdowns does not help for a nice UX.

I'll end this quick changelog with the [navbar](http://twitter.github.com/bootstrap/components.html#navbar) which is now gray by default. You can still get the old black one using the <code>.navbar-inverse</code> class.

I did a couple of changes to the website while upgrading to the new version of Bootstrap. Drop me a line if you have something to suggest or complain :)