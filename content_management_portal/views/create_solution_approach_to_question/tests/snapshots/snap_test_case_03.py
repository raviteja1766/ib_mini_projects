# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case status'] = 403

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case body'] = {
    'http_status_code': 403,
    'res_status': 'INVALID_QUESTION_EXCEPTION',
    'response': 'Please send valid question id'
}

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '114',
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
