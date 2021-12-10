from hypothesis import given
from hypothesis.strategies import integers, lists

from les_iterables import retain_if
from helpers.predicates import is_odd


@given(items=lists(integers()))
def test_retain_if_is_odd_retains_only_odd_integers(items):
    result = retain_if(is_odd, items)
    assert all(is_odd(x) for x in result)
