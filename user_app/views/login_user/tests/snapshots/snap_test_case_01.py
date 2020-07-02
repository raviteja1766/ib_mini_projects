# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginUserAPITestCase::test_case status'] = 200

snapshots['TestCase01LoginUserAPITestCase::test_case body'] = {
    'access_token': '1OfS6IZWCum8Jgpudp6FcAnqfKAb7t',
    'expires_in': '5189-04-11 09:51:25.278085',
    'refresh_token': 'SLnTl4l4z07mW7s96AlBcuXBhvVeid',
    'user_id': 1
}

snapshots['TestCase01LoginUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '159',
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
