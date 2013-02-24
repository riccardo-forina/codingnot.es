title: LESS is more
date: 2012-12-19
tags: [lesscss, flask]
abstract: "My css file was quite messy, so I decided for a fresh start with LESS. <br>Was it worthy?"

In short: **yes**!

Writing css with LESS will actually **save you a lot of keystroke**, even with the zen-coding/emmet plugin. The variable thing is something insanely useful. The other gem is the & operator: with it you can write very self-explanatory class dependencies.

## Using LESS with Flask

To integrate LESS with this website, I hade to change [the code](/recycling-part-2/) to integrate [Flask-Assets](http://elsdoerfer.name/docs/flask-assets/). Flask-Assets is a great tool that will add support for merging, minifying and compiling CSS and Javascript files.

To use it, in the application script add this code after the application declaration:

<pre class="prettyprint linenums">
from flask_assets import Environment
assets = Environment(application)
</pre>

Then in the base.html template change your CSS inclusion to this (modify it accordingly to your needs):

<pre class="prettyprint linenums">
{% assets filters="less", output="css/codingnotes.css", 'css/codingnotes.less' %}
&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;{{ ASSET_URL }}&quot;&gt;
{% endassets %}
</pre>

Flask-Assets will run your LESS file through lessc, compiling it to a normal css file.  
As a nice plus, it will add an hash to the file, good for client cache invalidation.

Just beware that using this kind of commodity may be not a great idea for very high traffic websites. If this is the case, you should aim for a build process.

## Use LESS on OpenShift

Flask-Assets will look for `lessc` in your PATH, but I couldn't find a way to install less with npm on my OpenShift server. This is the workaround I found (do it on your local machine):

- Activate project's virtualenv
- Install less through npm *without the `-g` flag*. This will create a `node_modules` directory in your project
- Add to the application script a `LESS_BIN` configuration to point to the newly installed module. In my case:  
`LESS_BIN = os.path.join(SCRIPT_ROOT, '..', 'node_modules', 'less', 'bin', 'lessc')`
- Add `node_mudules` and the changed files to git, then commit and push

Everything should work now!

## How does a LESS file look?

For the curious, this is my codingnotes.less file at the moment of writing:

<pre class="prettyprint linenums">
@bg-light: #FFF;
@bg-light-textcolor: #555152;
@bg-light-shadow: rgba(0, 0, 0, 1);
@bg-dark: #322F28;
@bg-dark-textcolor: #FAFAFA;
@bg-dark-shadow: #000;
@title-textcolor: #FA4B00;
@title-textcolor-hover: #E81300;
@header-font-family: 'Comfortaa', cursive;
@title-font-family: 'Abel', sans-serif;

body {
    background: @bg-dark;
    color: @bg-dark-textcolor;
}

body {
    > .container-fluid {
        padding-right: 0;
    }
}

.content {
    background: @bg-light;
    color: @bg-light-textcolor;
    border-left: 10px solid @title-textcolor;
}

.sidebar {
    aside {
        margin: 50px 0;
    }

    header {
        text-align: center;
    }
}

.link {
    color: @title-textcolor;
    &:hover {
        color: @title-textcolor-hover;
        text-decoration: none;
    }
}

.title {
    font-family: @title-font-family;
    font-weight: normal;
    line-height: 1.2;

    .sidebar & {
        color: @bg-dark-textcolor;
    }

    .content & {
        color: @title-textcolor;
    }
}

.siteHeader {
    text-align: center;
    font-size: 115%;
    .maintitle {
        font-family: @header-font-family;
        color: @bg-light;
        font-size: 220%;
        line-height: 2;
        b {
            color: @title-textcolor;
            &:hover {
                color: @title-textcolor-hover;
            }
        }
    }
}

.textShadow {
    .sidebar & {
        text-shadow: 1px 1px 0 @bg-dark, 3px 3px 0 @bg-dark-shadow;
    }
}

a {
    .link;
    .textShadow;
}

h1, h2, h3, h4, h5, h6 {
    .title;
    .textShadow;

}

.pages {
    article {
        margin: 50px 0;

        &:first-child {
            margin-top: 0;
        }
    }
}

.page {
    header {
        text-align: center;

        .abstract {
            font-size: 140%;
            line-height: 1.4;
        }
        margin: 50px 0;
    }
}

.published {
    display: block;
    font-size: 90%;
    min-height: inherit;
    line-height: 1.4;
    text-align: right;
    background: @title-textcolor;
    color: @bg-dark-textcolor;
    border-right: 5px solid @bg-dark;
    box-sizing: border-box;
    padding-right: 10px;

    span {
        font-weight: bold;
        font-size: 140%;
    }
}

.label {
    background-color: @bg-dark;
}

.badge {
    background-color: @title-textcolor;
}

.facebookframe {
    display: inline-block;
    border: none;
    width: 500px;
    height: 24px;
}

@media (max-width: 767px) {
    .published {
        border-right: 0;
        margin-bottom: 10px;
    }

    .facebookframe {
        width: 100%;
        margin-left: 0px;
    }
    .row-fluid .offset1:first-child {
        margin: 0;
    }
    .row-fluid [class*="span"] {
        padding: 0 10px;
    }
}
</pre>
