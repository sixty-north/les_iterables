from hypothesis import given
from hypothesis.strategies import integers, lists


from les_iterables.selecting import reject_truthy


@given(items=lists(integers()))
def test_reject_truthy(items):
    result = list(reject_truthy(items))
    assert not any(result)
