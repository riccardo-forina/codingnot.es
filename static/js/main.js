/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
var disqus_shortname = 'notesriccardoforina'; // required: replace example with your forum shortname
// var disqus_url = '';

(function($) {
  $(document).ready(function() {
    var qn = $('.quick-nav');
    $('article h2').each(function(idx) {
      var h2 = $(this),
          id = h2.text().toLowerCase()
                        .replace(/ /g,'-')
                        .replace(/[^\w-]+/g,'');
      h2.before('<span class="qna" id="' + id + '"><a href="#' + id + '"><i class="icon-tag-fill"></i></a></span>');
      qn.append('<li><a href="#' + id + '"><i class="icon-tag-fill"></i> ' + h2.text() + '</a></li>')
    });
    var titleHeight = $('h1').height();
    var body = $('body');
    $(window).scroll(function() {
      if ($(window).scrollTop() > titleHeight) {
        body.addClass('scrolling');
      } else {
        body.removeClass('scrolling');
      }
    });
  });

  /* * * DON'T EDIT BELOW THIS LINE * * */
  (function() {
      var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
      dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
      (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
  })();

  (function () {
      var s = document.createElement('script'); s.async = true;
      s.type = 'text/javascript';
      s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
      (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
  }());

})(jQuery);