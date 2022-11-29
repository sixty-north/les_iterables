from les_iterables.selecting import reject_if_none


def test_reject_if_none_yields_no_nones():
    actual = list(reject_if_none([1, 2, 3, None, 4, None, 5]))
    assert actual == [1, 2, 3, 4, 5]
