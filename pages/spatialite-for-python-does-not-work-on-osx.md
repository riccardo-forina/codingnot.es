title: Spatialite for Python does not work on OSX
date: 2012-08-08
tags: [python, sqlite, spatialite, osx]
abstract: The default Python shipped with OSX is not compatible with Spatialite. Lucky, there is a solution for that. Find more inside!

Is your OSX ready to work with the GIS extension for SQLite? Try doing this on a Python shell:

<pre class="prettyprint">
>>> import sqlite3
>>> conn = sqlite3.connect(':memory:')
>>> conn.enable_load_extension(True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'sqlite3.Connection' object has no attribute 'enable_load_extension'
</pre>

If you get the same error, welcome aboard!

The problem is that the Python interpreter shipped with OSX is not build with loadable extension support.

I'll quote the official documentation (I have had some troubles finding it):

<blockquote cite="http://docs.python.org/library/sqlite3.html#f1">
[1] (1, 2) The sqlite3 module is not built with loadable extension support by default, because some platforms (notably Mac OS X) have SQLite libraries which are compiled without this feature. To get loadable extension support, you must modify setup.py and remove the line that sets SQLITE_OMIT_LOAD_EXTENSION.
<small>Source: http://docs.python.org/library/sqlite3.html#f1</small>
</blockquote>

## How can I solve it?

You must install Python from scratch, enabling the loadable extension support at compile time.

You don't want to mess with sources and compilers? Me neither, so check my [How to setup correctly OSX for Python development](/how-to-setup-correctly-osx-for-python-development)