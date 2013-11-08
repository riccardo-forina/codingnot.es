title: Bootstrap your Django admin in 3 minutes
date: 2012-11-16
tags: [django, bootstrap, django-admin-bootstrapped]
abstract: And do it without changing your existing codebase!

Do you want Bootstrap on your Django admin app? You do not want to mess with the templates? That's why I did it for you!

## Updates

2013-11-08: Version bump to 1.6.0. *Django 1.6* compatibility (therefore the new version), experimental *Django-CMS 2.4* support, *Python 3* compatibility.
2013-05-29: Version bump to 0.4.1. Various bugfixes. See the CHANGELOG for more details  
2013-05-27: Version bump to 0.4. **Now compatibile with django-cms **. See the CHANGELOG for more details  
2013-02-06: list actions bugfix
2013-01-19: Registration template fixes
2013-01-17: Version bump to 0.3. Some UI cleaning and documentation. See the CHANGELOG for more details  
2012-12-19: Version bump to 0.2. Sortable inlines. See the CHANGELOG for more details  
2012-11-20: Version bump to 0.1.1. Couple of bugfixing, Bootstrap upgraded to version 2.2.1, etc. See the CHANGELOG for more details  
2012-11-16: Package addded to Pypi. You should now be able to pip install django-admin-bootstrapped. Thank Cyril for the help!

## What you'll get

- a responsive interface (because Bootstrap is)
- an heavy rewrite of the original django-admin templates, but with compatibility in mind.
- collapsable elements
- goodies like application name 'translations' without using the {% trans %} tag (to be documented)


## Requirements

Django 1.4.x

## Source code

On Github of course: [https://github.com/riccardo-forina/django-admin-bootstrapped](https://github.com/riccardo-forina/django-admin-bootstrapped)

## Installation

- <code>pip install django-admin-bootstrapped</code> (virtualenv highly suggested)
- add <code>django_admin_bootstrapped</code> into the INSTALLED_APPS list before <code>django.contrib.admin</code>
- have fun!

## Contribute!

This is not a complete project. I know for sure that the tabular inline form wil not work, because I didn't style it. Surely there will be edge cases, but still this is a project I used in production. Unluckly my time is quite limited, so every kind of help will be gladly appreciated!

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

## Screenshots

### Homepage

<img src="/static/screens/django_admin_bootstrapped_screen_v02_index.png">

### List view with filters in dropdown

<img src="/static/screens/django_admin_bootstrapped_screen_v02_list_filter.png">

### Change form view

<img src="/static/screens/django_admin_bootstrapped_screen_v02_change_form.png">
