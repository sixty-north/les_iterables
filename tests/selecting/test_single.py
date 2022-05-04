from pytest import raises

from les_iterables.selecting import single


def test_single_of_empty_raises_value_error():
    with raises(ValueError):
        _ = single([])


def test_single_of_single_returns_value():
    value = single([89])
    assert value == 89


def test_single_of_multiple_raises_value_error():
    with raises(ValueError):
        _ = single([89, 23])
