#!/usr/bin/env bash
PROJECT_PATH=$( cd $(dirname $0) ; pwd -P )
cd $PROJECT_PATH/frontend
npm run build
git add -A
git commit -m "deploy build"
git push origin master
cd $PROJECT_PATH/backend
./deploy.sh
