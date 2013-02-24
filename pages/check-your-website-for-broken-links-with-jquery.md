title: Check your website for broken links with jQuery
hide_push: true
date: 2012-08-10
updated: 2012-08-17
tags: [javascript, jquery, bootstrap, seo, status.js]
abstract: Broken links happens, but it's something you can check easily without any server side requirement. Just Javascript!

Writing my notes I make mistakes. I know, my English has room for improvement, but I do other mistakes like broken links, duplicate titles, empty meta descriptions...

A wise person would tell me: "hey dumbass, just download [Xenu's Link Sleuth](http://home.snafu.de/tilman/xenulink.html) and let it handle the dirty job!". You are completely right. But I'm a OSX user, as you [can see by my notes](/tag/osx), so Xenu is out of question. And I want something easier, maybe integrated in my website.

So I wrote Status.js!

<hr>

## Updates

### 2012-08-17: Graph plotting and sitemap.xml generator

A table is useful, but sometimes something more graphic is better. That's why I implemented the Javascript InfoVis Toolkit ([Jit](https://github.com/philogb/jit)) in Status.js to plot the website as a graph you can interact with.

Since I was coding, I wrote a dead easy sitemap.xml generator that makes use of the crawler work. Nothing fancy, but if you can't generate a sitemap in a more correct way it can be useful.

<hr>

# Status.js, a jQuery crawler

Let's start with an screenshot of what I'm talking about!

<img alt="Preview of Status.js" class="img-polaroid" src="/static/screens/status_beta_v01.png">

## Demo

You can see status.js at work on this site <a href="/status">here</a>.

<a href="https://github.com/riccardo-forina/status-jquery-crawler">Sources</a> on Github. Don't forget to star it!

## How does it work?

Status.js will scan the website it's hosted on from the root (/) for links.  
Internal links will be followed (fetched through Ajax) and scanned again. Yes, it's recursive.  
External links will be memorized and used for cross-referencies. You can't check if an external link is broken with Status.js because of the cross-domain limitation of Ajax calls.

A table with some nice data will be populated in real time while Status.js is working.

## How is it done?

Status.js is a [Backbone](http://documentcloud.github.com/backbone/) application.  
For Ajax and DOM manipulation, there is [jQuery](jquery.com).  
The url manipulation is powered by [jsUri](https://github.com/derek-watson/jsUri).  
The GUI part is [Twitter Bootstrap](http://twitter.github.com/bootstrap/).

For the details, I'll write a note in the future :D

## What can I check with Status.js?

### Url

The url of the page. To avoid duplication, hashes will be removed.

### Title

Available for internal pages only, the <code>title</code> tag is fetched. If not present, you'll get a <code>{No title}</code> placeholder.

### Description

Available for internal pages only, the <code>meta name="description"</code> tag is fetched. If not present, you'll get a <code>{No description}</code> placeholder.

### Status

Because of the Javascript-in-a-browser limitations, we can handle only these statuses:
<dl class="dl-horizontal">
<dt>Success</dt>
<dd>Available for internal pages only, means a correctly fetched page.</dd>
<dt>External</dt>
<dd>Indicates an external link.</dd>
<dt>Redirect</dt>
<dd>Indicates that there is another page for the same url but with a trailing slash. It's an hack around the browser that does not return any 30x http code</dd>
<dt>Error</dt>
<dd>_Broken link!_</dd>
<dt>Unfetched</dt>
<dd>Page memorized but waiting to be crawled.</dd>
</dl>

### Out links

It's the number of internal and external links present in the page. Clicking on the number you'll get the full list.

### In links

It's the number of pages that link to the url. Clicking on the number you'll get the full list.

## TODO list

This is a list of some of the things I'll have to work on. Please feel free to contribute with suggestions!

* Warnings about duplicate/too long/missing titles/descriptions.
* Verify for the presence of Google Analytics.
* Check for broken images
* Warning about missing/bad alt tags for images.
* Pagination
* Performance tests
* Let's be honest... _do_ tests!
* Code cleaning, comments, etc.

## Source code

The project is [available on Github](https://github.com/riccardo-forina/status-jquery-crawler). It's in a very early stage of development, so no documentation is provided.

If you want to try it, clone the repository, put the status folder somewhere on the website you want to check, open the status.html page with your browser and cross your fingers.

## Broken link

I'll put here a broken link to test the tool. [Don't click me!](/broken)

Have fun!