title: Bootstrap your Django admin in 3 minutes
date: 2012-11-16
tags: [django, bootstrap, django-admin-bootstrapped]
abstract: And do it without changing your existing codebase!


Do you want Bootstrap on your Django admin app? You do not want to mess with the templates? That's why I did it for you!

[![PyPI version](https://pypip.in/d/django-admin-bootstrapped/badge.png)](https://pypi.python.org/pypi/django-admin-bootstrapped)

## What you'll get

- a responsive interface (because Bootstrap is)
- an heavy rewrite of the original django-admin templates, but with compatibility in mind.
- collapsable elements
- goodies like application name 'translations' without using the {% trans %} tag (to be documented)
- you can choose between Bootstrap 2 and Bootstrap 3

## Requirements

Django >= 1.4.x

## Source code

On Github of course: [https://github.com/riccardo-forina/django-admin-bootstrapped](https://github.com/riccardo-forina/django-admin-bootstrapped)

## Installation

- <code>pip install django-admin-bootstrapped</code> (virtualenv highly suggested)
- add <code>django_admin_bootstrapped</code> into the INSTALLED_APPS list before <code>django.contrib.admin</code>
- have fun!

Your `INSTALLED_APPS` should look like this:


    INSTALLED_APPS = (
        'django_admin_bootstrapped',
        'django.contrib.admin',

        ...
    )

### Switch to Bootstrap3

*Available from version 1.6.2:* Do the previous steps, then add `'django_admin_bootstrapped.bootstrap3'` into the `INSTALLED_APPS` list __before__ `'django_admin_bootstrapped'`.

Your `INSTALLED_APPS` should look like this:


    INSTALLED_APPS = (
        'django_admin_bootstrapped.bootstrap3',
        'django_admin_bootstrapped',
        'django.contrib.admin',

        ...
    )

<img src="/static/screens/django_admin_bootstrapped3_screen_0.png">


## Goodies

### Translate/change an application name with a template

With the default admin you can't change the application name, but django-admin-bootstrapped let you do it in a really easy way. Just create a file named `admin_app_name.html` into the application's template folder. Eg: `myapp/templates/admin_app_name.html` or `project/templates/myapp/admin_app_name.html`.

### Add custom html to the change form of any model with a template

You can inject custom html on top of any change form creating a template named `admin_model_MODELNAME_change_form.html` into the application's template folder. Eg: `myapp/templates/admin_model_mymodelname_change_form.html` or `project/templates/myapp/admin_model_mymodelname_change_form.html`.

### Inline sortable

You can add drag&drop sorting capability to any inline with a couple of changes to your code.

First, add a `position` field in your model (and sort your model accordingly), for example:

<?prettify?>

    class TestSortable(models.Model):
        that = models.ForeignKey(TestMe)
        position = models.PositiveSmallIntegerField("Position")
        test_char = models.CharField(max_length=5)

        class Meta:
            ordering = ('position', )

Then in your admin.py create a class to handle the inline using the `django_admin_bootstrapped.admin.models.SortableInline` mixin, like this:

<?prettify?>

    from django_admin_bootstrapped.admin.models import SortableInline
    from models import TestSortable

    class TestSortable(admin.StackedInline, SortableInline):
        model = TestSortable
        extra = 0

You can now use the inline as usual. The result will look like this:

<img src="/static/screens/django_admin_bootstrapped_screen_inlines.png">

This feature was brought to you by [Kyle Bock](https://github.com/kwbock). Thank you Kyle!


### XHTML Compatible

Compatible with both html and xhtml.
To enable xhtml for your django app add the following to your settings.py:
DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'

### Generic lookups in admin

<img src="https://a248.e.akamai.net/camo.github.com/2848fec376b4af6d6a08e2a3a7d575569115f998/687474703a2f2f692e696d6775722e636f6d2f766970547453732e706e67" alt="Generic lookups in admin">

All that needs to be done is change the admin widget with either formfield_overrides like this:

<?prettify?>

    from django_admin_bootstrapped.widgets import GenericContentTypeSelect

    class SomeModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            models.ForeignKey: {'widget': GenericContentTypeSelect},
        }

Or if you want to be more specific:

<?prettify?>

    from django_admin_bootstrapped.widgets import GenericContentTypeSelect

    class SomeModelAdmin(admin.ModelAdmin):
        def formfield_for_dbfield(self, db_field, **kwargs):
            if db_field.name == 'content_type':
                kwargs['widget'] = GenericContentTypeSelect
            return super(SomeModelAdmin, self).formfield_for_dbfield(db_field, **kwargs)

If you decide on using `formfield_overrides` [you should be aware of its limitations with relation fields](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_overrides).

This feature (and many more) was brought to you by [Jacob Magnusson](https://github.com/jmagnusson). Thank you Jacob!


## Updates

==== 1.6.2 (2013-11-28) ====

- Bootstrap 3 theme (thanks to ze-phyr-us). In order to use it, add `django_admin_bootstrapped.bootstrap3` before `django_admin_bootstrapped` into your `INSTALLED_APPS` setting.

==== 1.6.1 (2013-11-16) ====

- FIX #56: jquery now loaded from local installation, not the CDN
- FIX #65: recent actions now has working urls

==== 1.6.0 (2013-11-08) ====

- django 1.6 compatibility
- experimental support to Django-CMS 2.4. This is thanks to a fork of kayluhb, which has never been transformed in a PR, but still it's worth a try.
- Python 3 compatibility (it has always been compatible, but now it's flagged appropriately as such)
- changed version to 1.6 to reflect the 'Stable' status of the project and the compatibility with Django 1.6

==== 0.4.3 (2013-08-27) ====

- display errors properly for inlines (thanks to jmagnusson)

==== 0.4.2 (2013-08-10) ====

- checkboxes now properly aligned
- admin title translation now working with a dedicated template

==== 0.4.1 (2013-05-29) ====

- tooltips for title attributes
- generic relation lookup plugin
- FIX: Twitter Bootstrap Responsive Navbar Broken on Small Screens (http://stackoverflow.com/questions/10185384/twitter-bootstrap-responsive-navbar-broken-on-small-screens) as reported by Fernando (https://twitter.com/fersan3)
- FIX: login page responsive layout
- FIX #6: autocapitalization disabled in the login form (mobile friendly)
- FIX #13: boolean fields will show the help text if provided
- FIX #36: list filters now partially usable on a mobile fine

==== 0.4 (2013-05-27) ====

- added compatibility for django-cms (thanks to kayluhb)
- xhtml cleanup (thanks to Ricklef Wohlers)
- UI cleanup (thanks to intuxicated & yceruto)
- Twitter Bootstrap version 2.3.1 (thanks to yceruto)
- admin static files now loaded using relative urls (thanks to jmagnusson)

==== 0.3.2 (2013-02-06) ====

- temporary bugfix for change_list actions

==== 0.3.1 (2013-01-19) ====

- registration template fixes


- registration template fixes

==== 0.3 (2013-01-17) ====

- dropped tabs in homepage in favour of vanilla list of available applications
- application dropdown menu for fast access in navbar
- filters moved to a dropdown in navbar to gain screen space
- added documentation for the translation goodies

==== 0.2 (2012-12-04) ====

- sortable inlines
- inlines wrapped in wells for UI consistency

==== 0.1.1 (2012-11-20) ====

- added a test project
- upgrade to Twitter Bootstrap 2.2.1 (issue #8)
- implemented inline tabular view
- fixed the messages styling
- temporary fix for the page title
- open is now the default style for the stacked inlines
- filters in the change list views are now positioned on the left, to handle wide tables
- pagination rendered with a smaller style (issue #2)

==== 0.1.0 (2012-10-22) ====

- first release


## Contribute!

This is not a complete project. I know for sure that the tabular inline form wil not work, because I didn't style it. Surely there will be edge cases, but still this is a project I used in production. Unluckly my time is quite limited, so every kind of help will be gladly appreciated!

## Screenshots

### Homepage

<img src="/static/screens/django_admin_bootstrapped_screen_v02_index.png">

### List view with filters in dropdown

<img src="/static/screens/django_admin_bootstrapped_screen_v02_list_filter.png">

### Change form view

<img src="/static/screens/django_admin_bootstrapped_screen_v02_change_form.png">
