from pytest import raises

from les_iterables.parsing import expand_numbered_list


def test_expand_numbered_list_empty():
    with raises(ValueError):
        list(expand_numbered_list(""))


def test_open_range_raises_value_error():
    with raises(ValueError):
        list(expand_numbered_list("42-"))


def test_expand_numbered_list_equal_start_and_end_raise_value_error():
    with raises(ValueError):
        list(expand_numbered_list("3-3"))


def test_expand_numbered_list_reversed_range_raises_error():
    with raises(ValueError):
        list(expand_numbered_list("2-1"))


def test_expand_number_list_single_term():
    assert list(expand_numbered_list("72")) == [72]


def test_expand_numbered_list_simple_range():
    assert list(expand_numbered_list("15-19")) == [15, 16, 17, 18, 19]


def test_expand_numbered_list_two_terms():
    assert list(expand_numbered_list("13, 67")) == [13, 67]


def test_expand_numbered_list_six_spaced_terms():
    assert list(expand_numbered_list("13, 67, 12, 88, 37, 11")) == [13, 67, 12, 88, 37, 11]


def test_expand_numbered_list_six_nonspaced_terms():
    assert list(expand_numbered_list("13,67,12,88,37,11")) == [13, 67, 12, 88, 37, 11]


def test_expand_numbered_list_six_semicolon_separated_terms():
    assert list(expand_numbered_list("13;67;12;88;37;11", separator=";")) == [13, 67, 12, 88, 37, 11]


def test_expand_numbered_list_with_ranges():
    assert list(expand_numbered_list("13, 67-72, 12, 88, 37-43, 11")) == [
        13, 67, 68, 69, 70, 71, 72, 12, 88, 37, 38, 39, 40, 41, 42, 43, 11]


def test_expand_numbered_list_with_non_default_ranges_separator():
    assert list(expand_numbered_list("13, 67-to-72, 12, 88, 37-to-43, 11", range_separator="-to-")) == [
        13, 67, 68, 69, 70, 71, 72, 12, 88, 37, 38, 39, 40, 41, 42, 43, 11]
