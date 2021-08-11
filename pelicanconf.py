#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = 'Headline'
SITESUBTITLE = 'Subtitle'
SITEURL = ''
ICON_URL= '/images/favicon.ico'
SITELOGO = '/images/logo.svg'

PATH = 'content'
THEME = '../Codeberg/NotMyIdea-Theme-Pelican/notmyidea/'
ALLOW_DARKTHEME = True
REMEMBER_DARKTHEME = True

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS_WIDGET_NAME = 'Links'
LINKS = (('Impressum', 'impressum'),
		 ('Datenschutzerklärung', 'datenschutz'),
		 ('Design-Quellcode', '#'))

# Social widget
SOCIAL_WIDGET_NAME = 'Kontakt'
SOCIAL = (('Email', 'mailto:email@example.org'),)

STATIC_PATHS = ['images']


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

