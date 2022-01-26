#!/usr/bin/env python3

# file py-rss-get.py

import feedparser, difflib
from difflib import *
from datetime import datetime, timedelta

dTobj = datetime.now()
timestamp_str_today = dTobj.strftime("%Y-%m-%d")

ydTobj = datetime.now() - timedelta(days=1)
timestamp_str_yesterday = ydTobj.strftime("%Y-%m-%d")

filename_today = "/usr/local/bin/py-rss/rss/pingdom-EU_" + timestamp_str_today + ".txt"
filename_yesterday = "/usr/local/bin/py-rss/rss/pingdom-EU_" +  timestamp_str_yesterday + ".txt"

print("")
print("===== py-rss -> get daily rss file ======================")
print("")
print("Today: " + filename_today + "\n")
print("Yesterday: " + filename_yesterday + "\n")
print("")
print("=========================================================")
print("")

f = open(filename_today, "w+")

feed_today = feedparser.parse('https://my.pingdom.com/probes/feed')

f.write(timestamp_str_today + "\n")

for entry in feed_today.entries:
        if (entry.pingdom_region == "EU"):
                f.write("\n=====\n" + entry.title + "\n" + entry.pingdom_ip + "\n" + entry.pingdom_hostname)
f.close()

