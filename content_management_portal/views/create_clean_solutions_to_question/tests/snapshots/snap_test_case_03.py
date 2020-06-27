# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateCleanSolutionsToQuestionAPITestCase::test_case status'] = 201

snapshots['TestCase01CreateCleanSolutionsToQuestionAPITestCase::test_case body'] = {
    'clean_solutions': [
        {
            'clean_solution_id': 1,
            'file_name': 'string2',
            'language': 'PYTHON',
            'solution_content': 'string'
        },
        {
            'clean_solution_id': 2,
            'file_name': 'string2',
            'language': 'PYTHON',
            'solution_content': 'string'
        },
        {
            'clean_solution_id': 3,
            'file_name': 'file_name_3',
            'language': 'C',
            'solution_content': 'code_3'
        },
        {
            'clean_solution_id': 4,
            'file_name': 'file_name_4',
            'language': 'RUBY',
            'solution_content': 'code_4'
        },
        {
            'clean_solution_id': 17,
            'file_name': 'string3',
            'language': 'PYTHON',
            'solution_content': 'string'
        },
        {
            'clean_solution_id': 18,
            'file_name': 'string4',
            'language': 'PYTHON',
            'solution_content': 'string'
        }
    ],
    'question_id': 1
}

snapshots['TestCase01CreateCleanSolutionsToQuestionAPITestCase::test_case header_params'] = {
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
