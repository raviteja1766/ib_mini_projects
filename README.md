# ib_miniprojects_backend


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
```

## install requirements

```bash
pip install -r requirements.txt

# if you ran into any issue with kerbrose package install below system dependencies
sudo apt-get install krb5-config libkrb5-dev libssl-dev libsasl2-dev libsasl2-modules-gssapi-mit python3.7-dev python3-dev -y

```

## running django management commands & usage

```sh
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=ib_miniprojects_backend.settings.local
python manage.py build -a mini_projects
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```