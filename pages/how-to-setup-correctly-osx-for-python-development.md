title: How to setup correctly OSX for Python development
date: 2012-08-08
tags: [python, osx, homebrew]
abstract: Let's setup OSX for Python development using homebrew and virtualenv.

OSX is great for Python development, because it ships with the interpreter preinstalled. But sometimes [you'll waste hours trying to make it work](/spatialite-for-python-does-not-work-on-osx) with your code.

So it's actually better to do not rely on what OSX gives you out of the box and install Python from scratch, but the easy way!

## Prerequisites

* a clean OSX installation (10.7 Lion or 10.8 Mountain Lion)
* no /usr/local folder
* Xcode installed
* [XQuartz](http://xquartz.macosforge.org/landing/) for formulae that require X11 libraries. Thanks Rust to [point it out on Hacker News](http://news.ycombinator.com/item?id=4361823).
* an internet connection

The procedure is quite easy, but __please consider that I will not be responsible for any loss or damage to your system__ that could result from following this how to.

## Step 1: install homebrew

[Homebrew](http://mxcl.github.com/homebrew/) is a package manager for OSX. Have you ever used apt-get/yum on Linux? Well, this is quite similar. By installing it you'll have access to a new command, brew, with which you'll be able to install, update, remove, search, etc., packages.

For a complete reference about installing options, refer to the [official documentation](https://github.com/mxcl/homebrew/wiki/Installation).

Open a Terminal and paste this line:

<pre class="prettylines">
ruby &lt;(curl -fsSk https://raw.github.com/mxcl/homebrew/go)
</pre>

You'll be guided through the installation process, so follow it carefully.

When it's done, you have brew installed but not ready to be used. First, do a sanity check of your environment:

<pre class="prettylines">
brew doctor
</pre>

It's very, very important that you solve all the problems it will bring up. If you have problems, try googling the error for insight or [contact me](#disqus_thread).

Now that brew is ready, you can fetch the newest version of it and all formulae from GitHub.

<pre class="prettylines">
brew update
</pre>

Now you have to update your <code>$PATH</code> to give priority to the software installed by brew.
Edit your <code>~/.bash_profile</code> file and add the following at the beginning:

<pre class="prettylines">
PATH=/usr/local/bin:$PATH
</pre>

Congratulation! Your system is ready :)

## Step 2: install Python

Now that we have brew installed and working, we can install Python.

<pre class="prettylines">
brew install python
</pre>

Homebrew will warn you that Python has been installed, but the default interpreter has not been touched. You can verify it typing:

<pre class="shell">
$ which python
/usr/bin/python
</pre>

Edit again your <code>~/.bash_profile</code> file and change the line we wrote before like this:

<pre class="prettylines">
PATH=/usr/local/bin:/usr/local/share/python:$PATH
</pre>

Close your terminal, open it again and verify that the default Python interpreter now is the one installed by brew.

<pre class="shell">
$ which python
/usr/local/bin/python
</pre>

As a nice plus, you'll have pip available to install your tools.

Have fun!