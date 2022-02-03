#!/bin/bash

FILE="/usr/local/bin/py-rss/results/changecheck.txt" #prod
#FILE="/mnt/vmshare/py-rss-gen2/py-rss/results/changecheck.txt" #lab
STRING="YES"

DATEVAR=`date +'%Y-%m-%d'`
CHANGEFILE=/usr/local/bin/py-rss/results/diffcheck-result_${DATEVAR}.txt
NOCHECKFILE=/usr/local/bin/mailtemplates/good.txt
SUBJECT="-PINGDOM SERVER CHECK- > Changes detected @ ${DATEVAR}"
SUBJECTNOCHANGES="-PINGDOM SERVER CHECK- > NO CHANGES @ ${DATEVAR}"

GIT=`which mail`
CAT=`which cat`



if grep -q "$STRING" "$FILE"; then
   echo "changecheck.txt contains >YES<";
   echo " -> there have been changes made in the pingdom server list!";
   echo "    -> sending an E-Mail with todays result file!";
    # Section
   cat ${CHANGEFILE} | mail -s "${SUBJECT}" pingdom-check@mairtech.de
    # Send-Email!
    #


else
    echo "changecheck.txt contains >NO<";
    echo " -> pingdom server list did not change!";
    echo "    -> days since the last change: :) ";
    cat ${NOCHECKFILE} | mail -s "${SUBJECTNOCHANGES}" marius.ehrhardt@itzbund.de
    # Section
    # Create "Days without Change counter!"
    #

fi