from les_iterables import single
from les_iterables.generating import one


def test_one():
    assert single(one(45)) == 45
