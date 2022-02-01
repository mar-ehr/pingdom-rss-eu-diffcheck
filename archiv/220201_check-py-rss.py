#!/usr/bin/env python3

#file py-rss-check.py

import difflib
from difflib import *
from datetime import datetime, timedelta

dTobj = datetime.now()
timestamp_str_today = dTobj.strftime("%Y-%m-%d")

ydTobj = datetime.now() - timedelta(days=1)
timestamp_str_yesterday = ydTobj.strftime("%Y-%m-%d")

filename_today = "/usr/local/bin/py-rss/rss/pingdom-EU_" + timestamp_str_today + ".txt"
filename_yesterday = "/usr/local/bin/py-rss/rss/pingdom-EU_" + timestamp_str_yesterday + ".txt"
filename_res_today = "/usr/local/bin/py-rss/results/diffcheck-result_" + timestamp_str_today + ".txt"

file_res_today = open(filename_res_today, "w")

#open today.txt as f, open yesterday,txt as g

with open(filename_today) as f, open(filename_yesterday) as g:
        flines = f.readlines()
        glines = g.readlines()

        d = difflib.Differ()
        diff = d.compare(flines, glines)
        #print("\n".join(diff))
        res1 = ("\n".join(diff))
        file_res_today.write("\n" + res1)
file_res_today.close()

res_plsamount = res1.count('+ ')
res_minamount = res1.count('- ')
res_qmamount = res1.count('? ')
print("")
print("======== py-rss -> diffcheck result ========")
print("")
print("Number of insertions (+) in results-file: " + str(res_plsamount))
print("Number of deletions (-) in results-file:  " + str(res_minamount))
print("Number of q-marks (?) in results-file:  " + str(res_qmamount))
print("")
print("======== ========================== ========")
print("")
