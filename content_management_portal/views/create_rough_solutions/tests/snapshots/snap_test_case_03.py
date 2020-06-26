# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case body'] = {
    'question_id': 1,
    'rough_solutions': [
        {
            'file_name': 'string2',
            'language': 'PYTHON',
            'rough_solution_id': 1,
            'solution_content': 'string'
        },
        {
            'file_name': 'string2',
            'language': 'PYTHON',
            'rough_solution_id': 2,
            'solution_content': 'string'
        },
        {
            'file_name': 'file_name_3',
            'language': 'C',
            'rough_solution_id': 3,
            'solution_content': 'code_3'
        },
        {
            'file_name': 'file_name_4',
            'language': 'RUBY',
            'rough_solution_id': 4,
            'solution_content': 'code_4'
        },
        {
            'file_name': 'string3',
            'language': 'PYTHON',
            'rough_solution_id': 17,
            'solution_content': 'string'
        },
        {
            'file_name': 'string4',
            'language': 'PYTHON',
            'rough_solution_id': 18,
            'solution_content': 'string'
        }
    ]
}

snapshots['TestCase01CreateRoughSolutionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '654',
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
