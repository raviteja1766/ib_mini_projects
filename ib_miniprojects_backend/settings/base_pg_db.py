import os

# ****************** Databases *************************
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
import uuid

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('RDS_DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
        'TEST': {
            'NAME': '/tmp/%s.sqlite3' % str(uuid.uuid4()),
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }
}
