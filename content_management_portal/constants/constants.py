DEFAULT_DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'




def check_for_none_values_of_offset_and_limit(offset, limit):
    if offset is None or limit is None:
        return 1, 8
    return offset, limit

def validate_offset(offset, total_questions_count):

    is_empty_questions = not total_questions_count
    if is_empty_questions:
        return True

    if offset < 1 or offset > total_questions_count:
        return False
    return True

def validate_limit(limit):

    if limit < 1 or limit > 10:
        return False
    return True