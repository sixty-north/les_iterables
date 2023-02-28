from les_iterables.sequences import prepend_unique


def test_prepend_unique_adds_items_to_empty_list():
    items = []
    added = prepend_unique(items, 1)
    assert items == [1]
    assert added


def test_prepend_unique_adds_items_to_non_empty_list():
    items = [1, 2, 3]
    added = prepend_unique(items, 4)
    assert items == [4, 1, 2, 3]
    assert added


def test_prepend_unique_does_not_add_duplicate_items():
    items = [1, 2, 3]
    added = prepend_unique(items, 2)
    assert items == [1, 2, 3]
    assert not added
