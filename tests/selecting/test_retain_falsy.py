from hypothesis import given
from hypothesis.strategies import integers, lists


from les_iterables.selecting import retain_falsy


@given(items=lists(integers()))
def test_retain_falsy(items):
    result = list(retain_falsy(items))
    assert not any(result)
