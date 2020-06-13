from content_management_portal.models import *


questions_dict = [
    {
        "short_text": "short_text1",
        "text_type": "TEXT",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text2",
        "text_type": "MARKDOWN",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text3",
        "text_type": "HTML",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text4",
        "text_type": "TEXT",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text5",
        "text_type": "MARKDOWN",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text6",
        "text_type": "HTML",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text7",
        "text_type": "TEXT",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text8",
        "text_type": "MARKDOWN",
        "description": "description1",
        "user": 1
    },
    {
        "short_text": "short_text9",
        "text_type": "HTML",
        "description": "description1",
        "user": 1
    }
]
Question.objects.bulk_create([
    Question(
        short_text=question_dict["short_text"],
        text_type=question_dict["text_type"],
        description=question_dict["description"],
        user_id=question_dict["user"]
    ) for question_dict in questions_dict
])

rough_solutions_dict = [
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 1,
        "user": 1
    },
    {
        "file_name": "hb",
        "language": "C",
        "code": "khufhfaff",
        "question": 2,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 3,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "RUBY",
        "code": "khufhfaff",
        "question": 2,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "JAVASCRIPT",
        "code": "khufhfaff",
        "question": 1,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 3,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 1,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 5,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 2,
        "user": 1
    },
    {
        "file_name": "java",
        "language": "PYTHON",
        "code": "khufhfaff",
        "question": 6,
        "user": 1
    }
]
RoughSolution.objects.bulk_create([
    RoughSolution(
        file_name=rough_dict["file_name"],
        language=rough_dict["language"],
        code=rough_dict["code"],
        question_id=rough_dict["question"],
        user_id=rough_dict["user"]
    ) for rough_dict in rough_solutions_dict
])
CleanSolution.objects.bulk_create([
    CleanSolution(
        file_name=rough_dict["file_name"],
        language=rough_dict["language"],
        code=rough_dict["code"],
        question_id=rough_dict["question"],
        user_id=rough_dict["user"]
    ) for rough_dict in rough_solutions_dict
])
PrefilledCode.objects.bulk_create([
    PrefilledCode(
        file_name=rough_dict["file_name"],
        language=rough_dict["language"],
        code=rough_dict["code"],
        question_id=rough_dict["question"],
        user_id=rough_dict["user"]
    ) for rough_dict in rough_solutions_dict
])