# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case body'] = {
    'question_id': 1,
    'solution_approach': {
        'complexity_analysis': {
            'content': 'string',
            'content_type': 'HTML'
        },
        'description': {
            'content': 'string',
            'content_type': 'HTML'
        },
        'solution_approach_id': 1,
        'title': 'string'
    }
}

snapshots['TestCase01CreateSolutionApproachToQuestionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '219',
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
