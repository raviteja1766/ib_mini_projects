from .base import *

LOGGING['handlers'].update({
    'logentries_pynamodb': {
        'level': 'DEBUG',
        'token': os.environ.get('LE_PYNAMODB_TOKEN', ''),
        'class': 'logentries.LogentriesHandler',
        'formatter': 'le_console',
        "filters": ["request_id", "user_id", "path_info",
                    "aws_request_id", "stage"],
    },
    'logentries_db': {
        'level': 'DEBUG',
        'token': os.environ.get('LE_DB_TOKEN', ''),
        'class': 'logentries.LogentriesHandler',
        'formatter': 'le_console',
        "filters": ["request_id", "user_id", "path_info",
                    "aws_request_id", "stage"],
    }
})

LOGGING['loggers'].update({
    'pynamodb': {
        'handlers': ['logentries_pynamodb'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'django.db.backends': {
        'handlers': ['logentries_db'],
        'level': 'DEBUG',
        'propagate': False,
    }
})
