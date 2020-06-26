# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case body'] = {
    'limit': 5,
    'offset': 1,
    'questions_list': [
        {
            'clean_solution_status': True,
            'prefilled_code_status': False,
            'question_id': 1,
            'rough_solution_status': False,
            'solution_approach_status': False,
            'statement': 'short_text_1',
            'test_cases_status': True
        },
        {
            'clean_solution_status': True,
            'prefilled_code_status': False,
            'question_id': 2,
            'rough_solution_status': False,
            'solution_approach_status': False,
            'statement': 'short_text_2',
            'test_cases_status': True
        },
        {
            'clean_solution_status': True,
            'prefilled_code_status': False,
            'question_id': 3,
            'rough_solution_status': False,
            'solution_approach_status': False,
            'statement': 'short_text_3',
            'test_cases_status': True
        },
        {
            'clean_solution_status': True,
            'prefilled_code_status': False,
            'question_id': 4,
            'rough_solution_status': False,
            'solution_approach_status': False,
            'statement': 'short_text_4',
            'test_cases_status': True
        },
        {
            'clean_solution_status': False,
            'prefilled_code_status': False,
            'question_id': 5,
            'rough_solution_status': False,
            'solution_approach_status': False,
            'statement': 'short_text_5',
            'test_cases_status': False
        }
    ],
    'total_questions': 8
}

snapshots['TestCase01GetCodingQuestionsDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1099',
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
