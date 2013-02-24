title: Use GoAccess to analyze your Amazon S3 logs
date: 2013-01-08
tags: [tool]
abstract: Just provide the correct format!

[GoAccess](http://goaccess.prosoftcorp.com/) is a neat tool to analyze any kind of web log fastly and even real-time. It supports out-of-the-box logs written in the following log format:

- Common Log Format (CLF) Apache
- Combined Log Format (XLF/ELF) Apache
- W3C format (IIS).
- Apache virtual hosts

Unluckly Amazon S3 uses a different log format, but with GoAccess it's not a problem since it can be configured to any custom format. How?

The [manpage](http://goaccess.prosoftcorp.com/man) lists the available parameters to define a custom log format, but I found nowhere a string compatible with Amazon S3 logs. With a little trial and error, here is a format that works:

`%^ %^ [%d:%^] %h %^ %^ %^ %^ "%^ %r %^" %s %^ %b %^ %^ %^ "%^" "%u" %^`



If you want to make it the default for every GoAccess run, edit (or create) a `~/.goaccessrc` file like this:

<pre>
date_format %d/%b/%Y
log_format %^ %^ [%d:%^] %h %^ %^ %^ %^ "%^ %r %^" %s %^ %b %^ %^ %^ "%^" "%u" %^
</pre>