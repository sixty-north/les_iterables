from les_iterables.sequences import extend_unique


def test_extend_unique_adds_items_to_empty_list():
    items = []
    added = extend_unique(items, [1, 3])
    assert items == [1, 3]
    assert added == {1, 3}


def test_extend_unique_adds_items_to_non_empty_list():
    items = [1, 2, 3]
    added = extend_unique(items, [4, 5])
    assert items == [1, 2, 3, 4, 5]
    assert added == {4, 5}


def test_extend_unique_does_not_add_duplicate_items():
    items = [1, 2, 3]
    added = extend_unique(items, [2, 3, 4])
    assert items == [1, 2, 3, 4]
    assert added == {4}
