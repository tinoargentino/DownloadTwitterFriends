#!/bin/bash

#Uploads changes to github and zip, creates deployment Zip file and uploads to AWS

git init
git config user.name "tinoargentino"
git config user.email "valentinsch@gmail.com"
git add .

IFS= read -r -p "Enter commit message: " input
# read varname
# $echo $varname
git commit -m "$input"

#IFS= read -r -p "Enter repo url: " repo
# read varname
# $echo $varname
# git commit -m "$repo"
git push
