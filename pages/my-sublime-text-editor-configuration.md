title: My Sublime Text Editor configuration
date: 2012-11-15
tags: [sublime text]
abstract: Because sharing is caring.

So I must share mine. Here's the complete list of what I _really_ use, in alphanumeric order. Plus a screenshot that's always nice.

<img alt="My ST" src="/static/screens/sublime.png">

##  Djaneiro

Django syntax and goodies.

##  emmet-sublime

AKA Zen-coding. I'm still in the getting known fase, sometime I like it, sometime I have to write more than what's needed. But that's just because me.

##  Generate Password

Need to generate a password on the fly? super+shift+p: password and you're done.

##  Git

I use this just to have a fast access to the changelog for the current file. But for the real work there is no way other than the terminal. Or the Git GUI if you're into that kind of stuff.

##  Http Requester

Pretty cool and easily forgotten tool to rapidly curl an address. Super useful to test that web service you always forget how to call.

##  Inc-Dec-Value

Capitalize-lowercase-uppercase-increment-decrement strings just by pressing a couple of buttons. Now, if I only could manage to remember 'em...

##  Line Completion

I dropped the heavy Intellisense plugin in favour of this supersimple completion based on what's already written on the file. 99% of the time it's the only thing I need.

##  LineEndings

Convert line endings. 'nuf said.

##  Modific

Modific is a  plugin for highlighting lines changed from the last commit. Not vital but cool. Too many dots on your bar and you should really start thinking about a commit.

##  Package Control

If you are reading this, you know it. If not, go grab it [_right now_](http://wbond.net/sublime_packages/package_control).

##  Prefixr

Do you get an headache every time you have to run through all the vendor-specific prefixes in your CSS code? Try [Prefixr](http://wbond.net/sublime_packages/prefixr), if you're lucky it will complete all the different variants for you. Unluckly I'm usually not lucky with it, it sort of ends messing up everything. Handle with care.

##  SideBarEnhancements

Directly from the readme:

<blockquote>
Notably provides delete as "move to trash", open with.. a and clipboard. Close, move, open and restore buffers affected by a rename/move command.

Provides the basics: new file/folder, edit, open/run, reveal, find in selected/parent/project, cut, copy, paste, paste in parent, rename, move, delete, refresh....

The not so basic: copy paths as URIs, URLs, content as UTF8, content as data:uri base64 ( nice for embedding into CSS! ), copy as tags img/a/script/style, duplicate

Preference to control if a buffer should be closed when affected by a deletion operation.

Allows to display "file modified date" and "file size" on statusbar.
</blockquote>

##  SublimeLinter

What I love about it is that now every Python code I write is nicely PEP8 compliant. What I don't love about it is when I open someone else Python script...

##  Theme - Phoenix

Well this is a theme, but a configurable one! You really should [try it](https://github.com/netatoo/phoenix-theme).

##  TrailingSpaces

Remove trailing spaces from your file. Note that Sublime can trim your files automatically on every save, just put this in your user settings (super+shift+p: Settings - User):

<pre>
"trim_trailing_white_space_on_save": true
</pre>

Thanks to Ryan Seys for the suggestion!



