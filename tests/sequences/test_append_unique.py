from les_iterables.sequences import append_unique


def test_append_unique_adds_items_to_empty_list():
    items = []
    added = append_unique(items, 1)
    assert items == [1]
    assert added


def test_append_unique_adds_items_to_non_empty_list():
    items = [1, 2, 3]
    added = append_unique(items, 4)
    assert items == [1, 2, 3, 4]
    assert added


def test_append_unique_does_not_add_duplicate_items():
    items = [1, 2, 3]
    added = append_unique(items, 2)
    assert items == [1, 2, 3]
    assert not added

