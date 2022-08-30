#!/usr/bin/env python3

#file py-rss-check.py

import difflib
from difflib import *
from datetime import datetime, timedelta

dTobj = datetime.now()
timestamp_str_today = dTobj.strftime("%Y-%m-%d")

ydTobj = datetime.now() - timedelta(days=1)
timestamp_str_yesterday = ydTobj.strftime("%Y-%m-%d")

#var_workingdir = "/mnt/vmshare/py-rss-gen2/py-rss" # lab
var_workingdir = "/usr/local/bin/py-rss" # prod

filename_today = var_workingdir + "/rss/pingdom-EU_" + timestamp_str_today + ".txt"
filename_yesterday = var_workingdir + "/rss/pingdom-EU_2022-08-24.txt"
filename_res_today = var_workingdir + "/results/diffcheck-result_" + timestamp_str_today + ".txt"

filename_checkingfile = var_workingdir + "/results/changecheck.txt"

file_res_today = open(filename_res_today, "w")

#open today.txt as f, open yesterday,txt as g

with open(filename_today) as f, open(filename_yesterday) as g:
        flines = f.readlines()
        glines = g.readlines()

        d = difflib.Differ()
        diff = d.compare(glines, flines)
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
file_changefile = open(filename_checkingfile, "w")
if ((res_plsamount == 1) and (res_qmamount == 2)):
        print(" No Changes - all good!")
        print("   -> NO > changecheck.txt")
        file_changefile.write("NO")
else: 
        print(" Pingdom Uptime Probe Server List changed!")
        print("   -> YES > changecheck.txt")
        file_changefile.write("YES")
file_changefile.close()
print("")
print("======== ========================== ========")
print("")

