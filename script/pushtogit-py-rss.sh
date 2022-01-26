#!/bin/bash

DATELOG=`date +'%Y-%m-%d %H:%M:%S'`
COMMIT-MESSAGE="shell-triggerd commit @ ${DATELOG}"

GIT=`which git`

REPO_DIR=/usr/local/bin/py-rss/
cd ${REPO_DIR}

echo ""
echo "automatic git add, commit & push @ ${DATELOG}"
echo ""
echo "=========================================================="
echo ""
echo "git add ...."

${GIT} add .

echo "=========================================================="
echo ""
echo "git commit wird ausgeführt mit folgender Commit-Message:"
echo ${COMMIT-MESSAGE}

${GIT} commit -m "${DATELOG}"

echo ""
echo "=========================================================="
echo ""
echo "pushe den commit in den master-branch des remote-repositories @ github"
echo ""

${GIT} push origin master

echo "=========================================================="
echo ""
echo "done!"


