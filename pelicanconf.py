#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#basic infos
AUTHOR = '彭斐'
SITENAME = '彭斐的博客'
SITEURL = 'https://fpeng1985.github.io'

SITELOGO = SITEURL + '/images/profile.jpg'

#time zone and language settings
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'ch'

#path settings
PATH = 'content'
PAGE_PATHS=['pages']
STATIC_PATHS=["images"]
PLUGIN_PATHS=["plugins"]

#category settings
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'

#URL settings
#RELATIVE_URLS = True
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Social settins
SOCIAL = (('github', 'https://github.com/fpeng1985'),
          ('twitter', 'https://twitter.com/fanta_hfut'),)

# Link settings
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#misc settings
DEFAULT_PAGINATION = 10
TYPOGRIFY = True

#Flex Theme settings
THEME = "themes/Flex"
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

SITETITLE = '彭斐'
SITESUBTITLE = 'Researcher - Programmer'
SITEDESCRIPTION = 'Research and programming.'

#menu settings
MAIN_MENU = True
MENUITEMS = (
    #('Home', '/index.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)



