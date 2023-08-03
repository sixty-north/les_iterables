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


def test_run_delimited_range_works():
    # TODO: break down this test
    assert run_delimited_range([1, 1, 1, 3, 3, 8, 15, 15, 15, 8, 18, 18]) == range(3, 10)
    assert run_delimited_range([-5, -1, 3, -8, 14, -2, -1], lambda a, b: a * b >= 0) == range(2, 5)
    assert run_delimited_range(["0", "1", "2", 3, 4, "5"], lambda a, b: type(a) == type(b)) == range(3, 5)
    assert run_delimited_range(["0", "1", "2", 3, 4, "5", 6, 7], lambda a, b: type(a) == type(b)) == range(3, 6)
    assert run_delimited_range('xxxxxxxxxxyyyyy') == range(10, 10)
