from les_iterables.searching import run_delimited_range

def test_empty_iterable_produces_empty_range():
    assert run_delimited_range([]) == range(0, 0)


def test_iterable_with_one_element_produces_empty_range():
    assert run_delimited_range('x') == range(1, 1)


def test_iterable_with_two_equal_elements_produces_empty_range():
    assert run_delimited_range('xx') == range(2, 2)


def test_iterable_with_two_unequal_elements_produces_1_1_range():
    assert run_delimited_range('xy') == range(1, 1)


def test_iterable_with_three_unequal_elements_produces_1_2_range():
    assert run_delimited_range('xyz') == range(1, 2)


def test_run_delimited_range_works_for_a_string():
    assert run_delimited_range('xxxxxxxxxxyyyyy') == range(10, 10)


def test_run_delimited_range_works_for_a_list_of_integers():
    assert run_delimited_range([1, 1, 1, 3, 3, 8, 15, 15, 15, 8, 18, 18]) == range(3, 10)


def test_run_delimited_range_works_with_a_sign_comparator():
    assert run_delimited_range([-5, -1, 3, -8, 14, -2, -1], lambda a, b: a * b >= 0) == range(2, 5)


def test_run_delimited_range_works_with_a_type_comparator_for_the_same_delimiter_type():
    assert run_delimited_range(["0", "1", "2", 3, 4, "5"], lambda a, b: type(a) == type(b)) == range(3, 5)


def test_run_delimited_range_works_with_a_type_for_different_delimiter_types():
    assert run_delimited_range(["0", "1", "2", 3, 4, "5", 6, 7], lambda a, b: type(a) == type(b)) == range(3, 6)
