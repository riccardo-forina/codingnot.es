title: Beware the jQuery.noConflict() monster!
date: 2012-08-03
tags: [jquery]
abstract: The intentions behind jQuery.noConflict() are good, but you will have problems if you are not careful.

jQuery.noConflict() is the [suggested way](http://docs.jquery.com/Using_jQuery_with_Other_Libraries) to use jQuery with other libraries. 

Basically, it prevents jQuery to replace the $ variable with a reference to itself, so that you can still use some other $ based javascript library together with jQuery.

## How does it work?

Try including Prototype and jQuery and print the $ variable.

<pre class="prettyprint linenums">
&lt;script src="https://ajax.googleapis.com/ajax/libs/prototype/1.7.1.0/prototype.js"&gt;&lt/script&gt;
&lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"&gt;&lt;/script&gt;
console.log($);
&gt;&gt;&gt; function() <- this is jQuery, any code that expects Prototype to be on the $ variabile will fail
&lt;/script&gt;
</pre>

But if you call the jQuery.noConflict() method, things will change.

<pre class="prettyprint linenums">
&lt;script src="https://ajax.googleapis.com/ajax/libs/prototype/1.7.1.0/prototype.js"&gt;&lt/script&gt;
&lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"&gt;&lt;/script&gt;
jQuery.noConflict();
console.log($);
&gt;&gt;&gt; $(element) <- this is Prototype, not jQuery!
console.log(jQuery);
&gt;&gt;&gt; function() <- this is jQuery, as expected
&lt;/script&gt;
</pre>

## So everything is cool and happy
Unlucky, it's not. If you rely on noConflict, you must be careful when including jQuery code from external sources - like your Wordpress plugins pool - because it is possible that the supercool plugin you wanna use uses the $ variable expecting jQuery, and not something else. Can you blame it?

Yes you can, because there is a super easy solution.

## The solution
In the [same page of the doc](http://docs.jquery.com/Using_jQuery_with_Other_Libraries), they suggest to wrap your jQuery based code like this:

<pre class="prettyprint linenums">
(function($) {
	/* some code that uses $ */ 
	$(document).ready(function() {
		console.log("$", $);
	});
})(jQuery)
</pre>

The above code declares a clousure (an anonymous function) which expects a $ parameter, and invokes it immediately passing the jQuery variable, _which will be always available if you included jQuery no matter what_. 

Et voilat! You can now write jQuery code using the $ shortcut without worrying about the noConflict monster.

The only drawback of this tecnique is that you will not be able to refer to other $ based libraries inside the closure, but… is this a real issue? For me, it has never been :)

Have fun!