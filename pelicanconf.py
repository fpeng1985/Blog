#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Theme 
THEME = "themes/Flex"

AUTHOR = '彭斐'
SITEDESCRIPTION = 'QCA technology research team.'
SITENAME = 'HFUT QCA'
SITEURL = ''
SITELOGO = SITEURL + '/images/profile.jpg'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)


TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'ch'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/fpeng1985'),
          ('twitter', 'https://twitter.com/fanta_hfut'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content'
STATIC_PATHS=["images"]
PLUGIN_PATHS=["plugins"]
