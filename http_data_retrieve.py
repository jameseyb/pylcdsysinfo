#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib.request
import feedparser

f = urllib.request.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
print(f.read(250).decode('utf-8'))

d = feedparser.parse(f)
d['feed']['title']
