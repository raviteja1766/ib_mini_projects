# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case status'] = 400

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_IDS_EXCEPTION',
    'response': 'Duplication of ids not accepted for updation'
}

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '126',
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
