from typing import List
from django.db.models import Prefetch, Count
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.models import (
    Question, Hint, TestCase, SolutionApproach
)
from content_management_portal.constants.enums import DescriptionType
from content_management_portal.interactors.storages.dtos import (
    QuestionDto, CodingQuestionDto, TestCaseDto, HintDto,
    QuestionCompleteDetailsDto, RoughSolutionDto,
    SolutionApproachDto, CleanSolutionDto, PrefilledCodeDto
)


class QuestionStorageImplementation(QuestionStorageInterface):

    def validate_question_id(self, question_id: int) -> bool:

        return Question.objects.filter(id=question_id).exists()

    def create_question(self, question_dto: QuestionDto) -> QuestionDto:

        question_obj = Question.objects.create(
            short_text=question_dto.short_text,
            text_type=question_dto.text_type,
            description=question_dto.description,
            user_id=question_dto.user_id
        )
        question_dto = self._convert_question_obj_to_dto(question_obj)
        return question_dto

    @staticmethod
    def _convert_question_obj_to_dto(question_obj):

        return QuestionDto(
            id=question_obj.id, short_text=question_obj.short_text,
            text_type=question_obj.text_type,
            description=question_obj.description,
            created_at=question_obj.created_at,
            user_id=question_obj.user_id
        )

    def update_question(self, question_dto: QuestionDto) -> QuestionDto:

        question_obj = Question.objects.get(id=question_dto.id)
        question_obj.short_text = question_dto.short_text
        question_obj.text_type = question_dto.text_type
        question_obj.description = question_dto.description
        question_obj.save()
        question_dto = self._convert_question_obj_to_dto(question_obj)

        return question_dto

    def get_user_to_question(self, question_id: int) -> int:

        question_obj = Question.objects.get(id=question_id)
        return question_obj.user_id

    def get_total_questions_count(self) -> int:

        return len(Question.objects.all())

    def get_coding_questions_details_dto(
            self, offset: int, limit: int) -> List[CodingQuestionDto]:

        question_objs = Question.objects\
            .select_related('solutionapproach')\
            .annotate(
                rough_solutions=Count('roughsolution'),
                test_cases=Count('testcase'),
                prefilled_codes=Count('prefilledcode'),
                clean_solution=Count('cleansolution')
            )
        return [
            self._convert_question_obj_to_coding_question_dto(question_obj)
            for question_obj in question_objs[offset-1: offset+limit-1]
        ]

    @staticmethod
    def _convert_question_obj_to_coding_question_dto(question_obj):

        solution_approach_count = 1
        try:
            question_obj.solutionapproach
        except SolutionApproach.DoesNotExist:
            solution_approach_count = 0

        return CodingQuestionDto(
            question_id=question_obj.id,
            short_text=question_obj.short_text,
            rough_solutions=question_obj.rough_solutions,
            test_cases=question_obj.test_cases,
            prefilled_code=question_obj.prefilled_codes,
            solution_approach=solution_approach_count,
            clean_solution=question_obj.clean_solution
        )

    def get_complete_question_details_dto(self, question_id: int):

        queryset = Hint.objects.all().order_by('order_id')
        query_set = TestCase.objects.all().order_by('order_id')
        question_obj = Question.objects\
            .filter(id=question_id)\
            .select_related('solutionapproach')\
            .prefetch_related(
                'roughsolution_set',
                'cleansolution_set',
                'solutionapproach',
                Prefetch('hint_set',queryset=queryset),
                Prefetch('testcase_set',queryset=query_set)
            ).first()

        return self._get_complete_details_for_question(question_obj)

    def _get_complete_details_for_question(self, question_obj):
        question_dto = self._convert_question_obj_to_dto(question_obj)
        rough_solutions_dto = self._get_roughsolution_objs_dto_to_question(
            question_obj=question_obj)
        prefilled_codes_dto = self._get_prefilled_code_objs_dto_to_question(
            question_obj=question_obj)
        clean_solutions_dto = self._get_clean_solution_objs_dto_to_question(
            question_obj=question_obj)
        solution_approach_dto = self._get_solution_approach_obj_dto_to_question(
            question_obj=question_obj)
        hints_dto = self._get_hint_objs_dto_to_question(
            question_obj=question_obj)
        test_cases_dto = self._get_test_case_objs_dto_to_question(
            question_obj=question_obj)
        return (question_dto, rough_solutions_dto, test_cases_dto,
                prefilled_codes_dto, solution_approach_dto,
                clean_solutions_dto, hints_dto)

    def _get_roughsolution_objs_dto_to_question(self, question_obj):

        rough_solution_objs = question_obj.roughsolution_set.all()
        rough_solutions_dto = self._convert_roughsolution_objs_to_dto(
            rough_solution_objs=rough_solution_objs)
        return rough_solutions_dto

    def _get_prefilled_code_objs_dto_to_question(self, question_obj):

        prefilled_code_objs = question_obj.prefilledcode_set.all()
        prefilled_codes_dto = self._convert_prefilled_code_objs_to_dto(
            prefilled_code_objs=prefilled_code_objs)
        return prefilled_codes_dto

    def _get_clean_solution_objs_dto_to_question(self, question_obj):

        clean_solution_objs = question_obj.cleansolution_set.all()
        clean_solutions_dto = self._convert_clean_solution_objs_to_dto(
            clean_solution_objs=clean_solution_objs)

        return clean_solutions_dto

    def _get_solution_approach_obj_dto_to_question(self, question_obj):

        try:
            solution_approach_obj = question_obj.solutionapproach
        except SolutionApproach.DoesNotExist:
            return None
        solution_approach_dto = self._convert_solutionapproach_to_dto(
            solution_approach_obj=solution_approach_obj)

        return solution_approach_dto

    def _get_hint_objs_dto_to_question(self, question_obj):

        hint_objs = question_obj.hint_set.all()
        hints_dto = self._convert_hint_objs_to_dto(hint_objs=hint_objs)

        return hints_dto

    def _get_test_case_objs_dto_to_question(self, question_obj):

        test_case_objs = question_obj.testcase_set.all()
        test_cases_dto = self._convert_test_case_objs_to_dto(
            test_case_objs=test_case_objs)
        return test_cases_dto

    @staticmethod
    def _convert_test_case_objs_to_dto(test_case_objs):

        return [
            TestCaseDto(
                id=test_case_obj.id,
                input_text=test_case_obj.input_text,
                output_text=test_case_obj.output_text,
                score=test_case_obj.score,
                is_hidden=test_case_obj.is_hidden,
                order_id=test_case_obj.order_id,
                question_id=test_case_obj.question_id,
                user_id=test_case_obj.user_id
            ) for test_case_obj in test_case_objs
        ]

    @staticmethod
    def _convert_hint_objs_to_dto(hint_objs):

        return [
            HintDto(
                id=hint_obj.id,
                title=hint_obj.title,
                content_type=hint_obj.content_type,
                content=hint_obj.content,
                order_id=hint_obj.order_id,
                question_id=hint_obj.question_id,
                user_id=hint_obj.user_id
            ) for hint_obj in hint_objs
        ]

    @staticmethod
    def _convert_solutionapproach_to_dto(solution_approach_obj):

        return SolutionApproachDto(
            id=solution_approach_obj.id,
            title = solution_approach_obj.title,
            description_content_type = \
                solution_approach_obj.description_content_type,
            description_content = \
                solution_approach_obj.description_content,
            complexity_content = \
                solution_approach_obj.complexity_content,
            complexity_content_type = \
                solution_approach_obj.complexity_content_type,
            question_id=solution_approach_obj.question_id,
            user_id=solution_approach_obj.user_id
        )

    @staticmethod
    def _convert_clean_solution_objs_to_dto(clean_solution_objs):

        return [
            CleanSolutionDto(
                id=clean_solution_obj.id,
                file_name=clean_solution_obj.file_name,
                language_type=clean_solution_obj.language,
                text_code=clean_solution_obj.code,
                question_id=clean_solution_obj.question_id,
                user_id=clean_solution_obj.user_id
            ) for clean_solution_obj in clean_solution_objs
        ]

    @staticmethod
    def _convert_prefilled_code_objs_to_dto(prefilled_code_objs):

        return [
            PrefilledCodeDto(
                id=prefilled_code_obj.id,
                file_name=prefilled_code_obj.file_name,
                language_type=prefilled_code_obj.language,
                text_code=prefilled_code_obj.code,
                question_id=prefilled_code_obj.question_id,
                user_id=prefilled_code_obj.user_id
            ) for prefilled_code_obj in prefilled_code_objs
        ]

    @staticmethod
    def _convert_roughsolution_objs_to_dto(rough_solution_objs):

        return [
            RoughSolutionDto(
                id=rough_solution_obj.id,
                file_name=rough_solution_obj.file_name,
                language_type=rough_solution_obj.language,
                text_code=rough_solution_obj.code,
                question_id=rough_solution_obj.question_id,
                user_id=rough_solution_obj.user_id
            ) for rough_solution_obj in rough_solution_objs
        ]


    def get_user_ids_of_questions(self, question_ids: List[int]):

        user_ids = Question.objects.filter(id__in=question_ids)\
            .values_list('user_id', flat=True)
        return user_ids

    def get_valid_question_ids(self, question_ids: List[int]):

        question_ids = Question.objects.filter(id__in=question_ids)\
            .values_list('id', flat=True)
        return question_ids
