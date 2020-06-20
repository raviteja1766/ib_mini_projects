

def my_sum(a, b):
    return a + b


def test_mything_when_both_positive_values(snapshot):

    a, b = 6, 7
    return_value = my_sum(a, b)
    snapshot.assert_match(return_value, 'gpg_response')


def test_mything_when_both_float_values(snapshot):

    a, b = 6.0, 7.0
    return_value = my_sum(a, b)
    snapshot.assert_match(return_value, 'gpg_response')


def test_mything_when_both_negative_values(snapshot):

    a, b = -6, -7
    return_value = my_sum(a, b)
    snapshot.assert_match(return_value, 'gpg_response')

def test_mything_when_both_positive_and_negative_given(snapshot):

    a, b = -6, 7
    return_value = my_sum(a, b)
    snapshot.assert_match(return_value, 'gpg_response')

