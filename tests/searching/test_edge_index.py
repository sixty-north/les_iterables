from les_iterables.searching import edge_index


def test_positive_edge_index_empty():
    assert edge_index([], +1) == -1


def test_positive_edge_index_single_truthy_item():
    assert edge_index([1], +1) == -1


def test_positive_edge_index_single_falsy_item():
    assert edge_index([0], +1) == -1


def test_positive_edge_index_only_falsy_items():
    assert edge_index([0, 0, 0], +1) == -1


def test_positive_edge_index_only_truthy_items():
    assert edge_index([1, 1, 1], +1) == -1


def test_positive_edge_index_first_item_falsy():
    assert edge_index([0, 1], +1) == 1


def test_positive_edge_index_first_item_truthy():
    assert edge_index([1, 0], +1) == -1


def test_find_second_positive_edge():
    assert edge_index([0, 1, 0, 1], +1, 1) == 3


def test_negative_before_positive_edge_ignores_negative_edge():
    assert edge_index([1, 0, 1], +1) == 2


def test_returns_first_of_many_positive_edges():
    assert edge_index([0, 0, 0, 1, 0, 1, 0, 1], +1) == 3


def test_negative_edge_index_empty():
    assert edge_index([], -1) == -1


def test_negative_edge_index_single_truthy_item():
    assert edge_index([1], -1) == -1


def test_negative_edge_index_single_falsy_item():
    assert edge_index([0], -1) == -1


def test_negative_edge_index_only_falsy_items():
    assert edge_index([0, 0, 0], -1) == -1


def test_negative_edge_index_only_truthy_items():
    assert edge_index([1, 1, 1], -1) == -1


def test_negative_edge_index_first_item_falsy():
    assert edge_index([0, 1], -1) == -1


def test_negative_edge_index_first_item_truthy():
    assert edge_index([1, 0], -1) == 1


def test_positive_before_negative_edge_ignores_positive_edge():
    assert edge_index([0, 1, 0], -1) == 2


def test_returns_first_of_many_negative_edges():
    assert edge_index([1, 1, 1, 0, 1, 0, 1, 0], -1) == 3


def test_find_second_negative_edge():
    assert edge_index([1, 0, 1, 0], -1, 1) == 3


