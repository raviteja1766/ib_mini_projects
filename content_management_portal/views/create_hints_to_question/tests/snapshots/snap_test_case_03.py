# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateHintsToQuestionAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateHintsToQuestionAPITestCase::test_case body'] = {
    'hint': {
        'description': {
            'content': 'string',
            'content_type': 'HTML'
        },
        'hint_id': 1,
        'hint_number': 1,
        'title': 'string'
    },
    'question_id': 1
}

snapshots['TestCase01CreateHintsToQuestionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '141',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
