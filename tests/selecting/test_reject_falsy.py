from hypothesis import given
from hypothesis.strategies import integers, lists

from les_iterables import reject_falsy


@given(items=lists(integers()))
def test_reject_falsy(items):
    result = reject_falsy(items)
    assert all(result)
