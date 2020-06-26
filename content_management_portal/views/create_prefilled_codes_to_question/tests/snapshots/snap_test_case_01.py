# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreatePrefilledCodesToQuestionAPITestCase::test_case status'] = 400

snapshots['TestCase01CreatePrefilledCodesToQuestionAPITestCase::test_case body'] = [
    {
        'file_name': [
            'This field is required.'
        ],
        'language': [
            'This field is required.'
        ],
        'solution_content': [
            'This field is required.'
        ]
    }
]

snapshots['TestCase01CreatePrefilledCodesToQuestionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '129',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
