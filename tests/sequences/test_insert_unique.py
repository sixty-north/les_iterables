from les_iterables.sequences import insert_unique


def test_insert_unique_adds_items_to_empty_list():
    items = []
    added = insert_unique(items, 0, 1)
    assert items == [1]
    assert added


def test_insert_unique_adds_items_to_non_empty_list():
    items = [1, 2, 3]
    added = insert_unique(items, 1, 4)
    assert items == [1, 4, 2, 3]
    assert added


def test_insert_unique_does_not_add_duplicate_items():
    items = [1, 2, 3]
    added = insert_unique(items, 1, 2)
    assert items == [1, 2, 3]
    assert not added

