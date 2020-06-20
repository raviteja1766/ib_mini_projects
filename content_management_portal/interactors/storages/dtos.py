import datetime
from dataclasses import dataclass
from typing import List, Optional
from content_management_portal.constants.enums\
    import DescriptionType, CodeLanguageType


@dataclass()
class AccessTokenDTO:
    access_token_id: int
    token: str
    expires: datetime.datetime


@dataclass()
class QuestionDto:
    id: int
    short_text: str
    text_type: DescriptionType
    description: str
    created_at: datetime.datetime
    user_id: int


@dataclass()
class RoughSolutionDto:
    id: Optional[int]
    file_name: str
    language_type: CodeLanguageType
    text_code: str
    question_id: int
    user_id: int

@dataclass()
class SolutionDto:
    id: Optional[int]
    file_name: str
    language_type: CodeLanguageType
    text_code: str
    question_id: int
    user_id: int

@dataclass()
class CodingQuestionDto:
    question_id: int
    short_text: str
    rough_solutions: bool
    test_cases: bool
    prefilled_code: bool
    solution_approach: bool
    clean_solution: bool


@dataclass()
class QuestionCompleteDetailsDto:
    question_dto: QuestionDto
    rough_solutions_dto: List[RoughSolutionDto]


@dataclass()
class TestCaseDto:
    id: Optional[int]
    input_text: Optional[str]
    output_text: Optional[str]
    score: int
    is_hidden: bool
    order_id: Optional[int]
    question_id: int
    user_id: int


@dataclass()
class PrefilledCodeDto:
    id: Optional[int]
    file_name: str
    language_type: CodeLanguageType
    text_code: str
    question_id: int
    user_id: int


@dataclass()
class CleanSolutionDto:
    id: Optional[int]
    file_name: str
    language_type: CodeLanguageType
    text_code: str
    question_id: int
    user_id: int

@dataclass()
class SolutionApproachDto:
    id: Optional[int]
    title: str
    description_content_type: DescriptionType
    description_content: str
    complexity_content_type: DescriptionType
    complexity_content: str
    question_id: int
    user_id: int


@dataclass()
class HintDto:
    id: Optional[int]
    title: str
    content_type: DescriptionType
    content: str
    order_id: Optional[int]
    question_id: int
    user_id: int

@dataclass()
class TestCaseSwapDto:
    id: int
    order_id: int


@dataclass()
class HintSwapDto:
    id: int
    order_id: int
