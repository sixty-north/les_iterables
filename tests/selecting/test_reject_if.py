from hypothesis import given
from hypothesis.strategies import lists, integers

from les_iterables import reject_if
from helpers.predicates import is_odd, is_even


@given(items=lists(integers()))
def test_reject_if_is_odd_retains_only_even_integers(items):
    result = reject_if(is_odd, items)
    assert all(is_even(x) for x in result)