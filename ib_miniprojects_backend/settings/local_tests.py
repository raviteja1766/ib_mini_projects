import uuid

from ib_miniprojects_backend.settings.local import *
from ib_miniprojects_backend.settings.base_pg_db import *

DATABASES['default']['TEST'].update({
    'NAME':  str(uuid.uuid4()),
    'ENGINE': os.environ.get('RDS_DB_ENGINE'),
    'CHARSET': 'UTF8'
})

