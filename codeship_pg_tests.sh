#!/bin/bash

# configure default django settings
export DJANGO_SETTINGS_MODULE="ib_miniprojects_backend.settings.local_tests"

echo "Executing Tests on Postgres DB on codeship"

export RDS_PASSWORD="test"
export RDS_DB_ENGINE="django.db.backends.postgresql_psycopg2"
export RDS_DB_NAME="test_db"
export RDS_USERNAME="postgres"
export RDS_PORT=5432
export RDS_HOSTNAME="127.0.0.1"

# run management commands
python manage.py $@
