#!/bin/bash

# configure default django settings
export DJANGO_SETTINGS_MODULE="ib_miniprojects_backend.settings.local_tests"

echo "Executing Tests on MySQL DB on codeship"

# configure env variables
export RDS_PASSWORD="test"
export RDS_DB_ENGINE="django.db.backends.mysql"
export RDS_DB_NAME="test_db"
export RDS_USERNAME="root"
export RDS_PORT=3306
export RDS_HOSTNAME="127.0.0.1"

# creating database
echo "create database $RDS_DB_NAME DEFAULT CHARACTER SET utf8 ;" | mysql -p${RDS_PASSWORD} -h ${RDS_HOSTNAME} -u root

# run management commands
python manage.py $@
