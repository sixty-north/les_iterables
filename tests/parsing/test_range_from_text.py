from pytest import raises

from les_iterables.parsing import range_from_text


def test_range_from_text_empty():
    with raises(ValueError):
        range_from_text("")


def test_range_from_text_non_numeric():
    with raises(ValueError):
        range_from_text("NOT A NUMBER")


def test_range_from_text_single_number():
    assert range_from_text("5") == range(5, 6)


def test_range_from_text_single_element_range():
    assert range_from_text("5-5") == range(5, 6)


def test_range_from_text_two_element_range():
    assert range_from_text("5-6") == range(5, 7)


def test_range_from_text_ten_element_range():
    assert range_from_text("5-15") == range(5, 16)


def test_range_from_text_ten_element_range_space_before():
    assert range_from_text("  5-15") == range(5, 16)


def test_range_from_text_ten_element_range_space_after():
    assert range_from_text("5-15   ") == range(5, 16)


def test_range_from_text_ten_element_range_space_between():
    assert range_from_text("5 - 15") == range(5, 16)


def test_range_from_text_two_element_range_non_default_separator():
    assert range_from_text("5—-6", separator="—-") == range(5, 7)


def test_range_from_negative_raises_value_error():
    with raises(ValueError):
        range_from_text("-5 - 15")


def test_descending_range_raises_value_error():
    with raises(ValueError):
        range_from_text("2-1")
