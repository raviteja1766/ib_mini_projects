#!/bin/bash
npm install apidoc
pip install virtualenv virtualenvwrapper
mkvirtualenv _ib_env
pip install -r requirements.txt
pip install -r requirements_deploy.txt
DJANGO_SETTINGS_MODULE=ib_miniprojects_backend.settings."$1" python manage.py build -adj
DJANGO_SETTINGS_MODULE=ib_miniprojects_backend.settings."$1" python manage.py mocktests
DJANGO_SETTINGS_MODULE=ib_miniprojects_backend.settings."$1" python manage.py s3push -d --bucket swagger-apidocs --prefix ib_miniprojects_backend/"$1"
zappa update alpha
zappa manage "migrate --no-input"
