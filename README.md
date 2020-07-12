# kart
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04
* https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

## run local server
* flask run --host=0.0.0.0 --port=5000

## production server
* web: ngninx
* application: gunicorn / systemd name: `indicard`
* test gunicorn binding: `gunicorn --bind 0.0.0.0:5000 wsgi:guni`

## mongo config
* remember we're not running mongo on the application server
* start db server: `service mongodb start`

## deployment setup
* add git
* create ssh key (if needed): https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
* add key to github
* clone project

## deploy
* (from local) git push deploy master
* install from requirements: pip install -r requirements.txt
* run migrations
* restart application server
* unit tests

## git post-receive deploy config
#!/bin/sh
  
# The production directory
TARGET="/home/ubuntu/project/api"

# A temporary directory for deployment
TEMP="/home/ubuntu/project/tmp/api"

# The Git repo
REPO="/home/ubuntu/project/git/api.git"

# Deploy the content to the temporary directory
mkdir -p $TEMP
git --work-tree=$TEMP --git-dir=$REPO checkout -f

cd $TEMP
# Do stuffs, like npm install…

# Replace the production directory
# with the temporary directory
cp -r * $TARGET
cd /
rm -rf $TEMP

## env file

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=run
export FLASK_DEBUG=1
export FLASK_ENV=development

# braintree config
BT_ENVIRONMENT=''
BT_MERCHANT_ID=''
BT_PUBLIC_KEY=''
BT_PRIVATE_KEY=''

# settings config
FLASK_MODULE_SETTINGS=settings/production.py
