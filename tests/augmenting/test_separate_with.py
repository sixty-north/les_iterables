from les_iterables.augmenting import separate_with


def test_separate_with_empty_yields_empty():
    assert list(separate_with([], 5)) == []


def test_separate_with_single_yields_single():
    assert list(separate_with([7], 5)) == [7]


def test_separate_with_two_items_yields_three_items():
    assert list(separate_with([7, 2], 5)) == [7, 5, 2]


def test_separate_with_three_items_yields_five_items():
    assert list(separate_with([7, 2, 9], 5)) == [7, 5, 2, 5, 9]
