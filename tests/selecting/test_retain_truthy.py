from hypothesis import given
from hypothesis.strategies import integers, lists

from les_iterables import retain_truthy


@given(items=lists(integers()))
def test_retain_truthy(items):
    result = retain_truthy(items)
    assert all(result)
