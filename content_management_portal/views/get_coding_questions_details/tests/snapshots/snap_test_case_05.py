# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case status'] = 400

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT_LENGTH',
    'response': 'limit should be less than total number of questions  greater than zero'
}

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '149',
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
