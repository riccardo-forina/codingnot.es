title: "SASS and Inuit CSS"
date: 2013-10-21
tags: [sass]
abstract: SASS and Inuit CSS are a great combination to build any kind of website.

[Previously](/less-is-more/) I talked about my use of LESS for this website. It still true, but since then I found a little gem that made me switch to SASS for the best: [Inuit CSS](http://inuitcss.com).

## Inuit CSS

Inuit CSS is a _great_ framework built on solid BEM principles that gives you ready-to-use CSS classes to solve the most common problems you have while building a website. It's DRY bringed to CSS design.

To give you an example, why write code to handle an horizontal navigation bar when the basic of it is always the same? And the same applies to other design patterns, like pagination, breadcrumbs and so on.

This is a list of patterns Inuit gives you for free:

    grids, flexbox, columns, nav, options, pagination, breadcrumb, media, marginalia, island, block-list, matrix, split, this-or-this, link-complex, flyout, arrows, sprite, icon-text, beautons, lozenges, rules, stats, greybox

I used Inuit in a lot of projects and I never regret it, au contraire! It helped me to achieve great results in no time. Thank you [Harry Roberts](https://twitter.com/csswizardry)!

**If you need a CSS guru, Harry is [currently available](http://csswizardry.com/2013/10/lets-work-together/).**

## SASS

As I said, Inuit takes leverage from SASS capabilities. In fact with SASS you can write very complex features, thanks to features like loops.

To speak the truth, choosing SASS over LESS is just a matter of personal preferences. Tooling support is about the same, output code is almost the same in terms of generated selectors.

For a more in depth analysis you should check the [SASS vs LESS](http://css-tricks.com/sass-vs-less/) article by Chris Coyier.

## Inuit, SASS and this website

In short, I dumped Twitter Boootstrap in favor of my hand-made html powered by just the objects I needed from Inuit - `nav` and `flyout` - and you can see the result with your eyes.

Speaking of design choices, it's heavily inspired by the [Flatland](https://github.com/thinkpixellab/flatland) theme and color scheme for Sublime Text, plus the Ubuntu family fonts which I found great for readability.