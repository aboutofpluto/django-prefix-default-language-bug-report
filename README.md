# Simple django project to replicate bug report

## Bug report

https://code.djangoproject.com/ticket/34515

Related issue on `prefix_default_language`
https://code.djangoproject.com/ticket/34455

## How to

1. Install Django 4.2 (or event 4.2.1)

```
$ pip install django==4.2
```

2. Clone repository

```
$ git clone git@github.com:aboutofpluto/django-prefix-default-language-bug-report.git
```

3. Change directory

```sh
$ cd django-prefix-default-language-bug-report
```

4. Create translation files (be sure to get the 3 languages)

```sh
$ python manage.py compilemessages
File “/home/ab/work/django/prefix/locale/es/LC_MESSAGES/django.po” is already compiled and up to date.
File “/home/ab/work/django/prefix/locale/fr/LC_MESSAGES/django.po” is already compiled and up to date.
File “/home/ab/work/django/prefix/locale/en/LC_MESSAGES/django.po” is already compiled and up to date.
```

5. Run server

```sh
$ python manage.py runserver 127.0.0.1:8000
```

6. Open a browser and go to about page: http://127.0.0.1:8000/about/

7. Click on "En", "Fr", "Es".
Should work fine and redirect to:

- En: http://127.0.0.1:8000/about/
- Fr: http://127.0.0.1:8000/fr/a-propos/
- Es: http://127.0.0.1:8000/es/a-proposito/

8. Edit prefix/settings.py and change `LANGUAGE_CODE` to `'fr'`

9. Reload page in browser and click on "En", "Es", "Fr".
Should work fine for 'en' and 'es':

- En: http://127.0.0.1:8000/en/about/
- Es: http://127.0.0.1:8000/es/a-proposito/

but 'fr' will return 404 (http://127.0.0.1:8000/a-propos/)
