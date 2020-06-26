# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetQuestionCompleteDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetQuestionCompleteDetailsAPITestCase::test_case body'] = {
    'clean_solutions': [
        {
            'clean_solution_id': 1,
            'file_name': 'file_name_1',
            'language': 'PYTHON',
            'solution_content': 'code_1'
        },
        {
            'clean_solution_id': 2,
            'file_name': 'file_name_2',
            'language': 'JAVA',
            'solution_content': 'code_2'
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
        }
    ],
    'hints': [
        {
            'description': {
                'content': 'content_1',
                'content_type': 'MARKDOWN'
            },
            'hint_id': 1,
            'hint_number': 1,
            'title': 'title_1'
        },
        {
            'description': {
                'content': 'content_2',
                'content_type': 'HTML'
            },
            'hint_id': 2,
            'hint_number': 2,
            'title': 'title_2'
        },
        {
            'description': {
                'content': 'content_3',
                'content_type': 'LATEX'
            },
            'hint_id': 3,
            'hint_number': 3,
            'title': 'title_3'
        },
        {
            'description': {
                'content': 'content_4',
                'content_type': 'TEXT'
            },
            'hint_id': 4,
            'hint_number': 4,
            'title': 'title_4'
        }
    ],
    'prefilled_codes': [
        {
            'file_name': 'file_name_1',
            'language': 'PYTHON',
            'prefilled_code_id': 1,
            'solution_content': 'code_1'
        },
        {
            'file_name': 'file_name_2',
            'language': 'JAVA',
            'prefilled_code_id': 2,
            'solution_content': 'code_2'
        },
        {
            'file_name': 'file_name_3',
            'language': 'C',
            'prefilled_code_id': 3,
            'solution_content': 'code_3'
        },
        {
            'file_name': 'file_name_4',
            'language': 'RUBY',
            'prefilled_code_id': 4,
            'solution_content': 'code_4'
        }
    ],
    'question_id': 1,
    'rough_solutions': [
        {
            'file_name': 'file_name_1',
            'language': 'PYTHON',
            'rough_solution_id': 1,
            'solution_content': 'code_1'
        },
        {
            'file_name': 'file_name_2',
            'language': 'JAVA',
            'rough_solution_id': 2,
            'solution_content': 'code_2'
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
        }
    ],
    'solution_approach': {
        'complexity_analysis': {
            'content': 'complexity_content_1',
            'content_type': 'MARKDOWN'
        },
        'description': {
            'content': 'description_content_1',
            'content_type': 'MARKDOWN'
        },
        'solution_approach_id': 1,
        'title': 'title_1'
    },
    'statement': {
        'problem_description': {
            'content': 'description_1',
            'content_type': 'MARKDOWN'
        },
        'short_text': 'short_text_1'
    },
    'test_cases': [
        {
            'input': 'input_text_1',
            'is_hidden': True,
            'output': 'output_text_1',
            'score': 10,
            'test_case_id': 1,
            'test_case_number': 1
        },
        {
            'input': 'input_text_2',
            'is_hidden': True,
            'output': 'output_text_2',
            'score': 20,
            'test_case_id': 2,
            'test_case_number': 2
        },
        {
            'input': 'input_text_3',
            'is_hidden': True,
            'output': 'output_text_3',
            'score': 30,
            'test_case_id': 3,
            'test_case_number': 3
        },
        {
            'input': 'input_text_4',
            'is_hidden': True,
            'output': 'output_text_4',
            'score': 40,
            'test_case_id': 4,
            'test_case_number': 4
        }
    ]
}

snapshots['TestCase01GetQuestionCompleteDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '2711',
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
