from gyaan.exceptions.exceptions import InvalidOffsetValue, InvalidLimitValue


def check_for_none_values_of_offset_and_limit(offset, limit):
    if offset is None or limit is None:
        offset, limit = 0, 5
    return offset, limit

def validate_offset(offset):

    if offset < 0:
        raise InvalidOffsetValue

def validate_limit(limit):

    if limit < 1 or limit > 5:
        raise InvalidLimitValue
