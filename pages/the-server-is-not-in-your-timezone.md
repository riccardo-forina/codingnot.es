title: The server is not in your timezone
date: 2012-09-11
tags: [bookmark, datetime]
abstract: Scheduled a cron job that didn't start when expected? The problem is you!

99% of the time the problem is not in the scheduling, but in you not caring about how the server was configured in first place. Noah Sussman summarized a lot of falsehoods programmers believe about time [on his own website](http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time). Don't miss the updates!

As a quick hint, I can suggest sticking with UTC datetimes and _always_ normalize dates to it. If you're using Django, be sure to check the [time zones](https://docs.djangoproject.com/en/dev/topics/i18n/timezones/) (new in Django 1.4) support, it helps a lot.