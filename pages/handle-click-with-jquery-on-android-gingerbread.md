title: Click event not fired on Android 2.3.x
date: 2012-12-11
tags: [javascript]
abstract: Handle 'click' events in jQuery with support for the default browser shipped with Android Gingerbread (2.3.x)

This is something I discovered some time ago, but keeps popping out. Looks like the default browser shipped with Android Gingerbread (2.3.x) doesn't fire neither the `click` nor the `tap` event. Instead of them, it will fire the `touchstart` one.

The solution is handling the correct event based on the browser capability. An example solution is the following:

<pre class="prettyprint linenums">
var touch = ('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch;
var touchEvent = touch ? 'touchstart' : 'click';

$('#anItem').bind(touchEvent, function() {
  console.log("Touchclicked:", this);
});
</pre>

I made a [Gist](https://gist.github.com/4262757) of it, so if you have a better way to handle it please fork and let me know!

<small>Plus I had an excuse to use the [new GitHub Gist interface](https://github.com/blog/1276-welcome-to-a-new-gist), it's super cool!</small>