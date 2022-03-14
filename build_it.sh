#!/bin/bash
export DISPLAY=:0
echo "Build script for blog-spnet"
cd /home/spnet_user/blog-spnet
source spnetblogvenv/bin/activate
git pull origin main
make html
deactivate
