# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTestCasesAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateTestCasesAPITestCase::test_case body'] = {
    'question_id': 1,
    'test_case': {
        'input': 'string',
        'is_hidden': True,
        'output': 'string',
        'score': 10,
        'test_case_id': 1,
        'test_case_number': 1
    }
}

snapshots['TestCase01CreateTestCasesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '146',
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
