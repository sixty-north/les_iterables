from collections.abc import Generator

from les_iterables.generating import generate


def test_generate_default_returns_generator():

    @generate()
    def generator_function():
        yield 1
        yield 2
        yield 3

    g = generator_function()
    assert isinstance(g, Generator)


def test_generate_list_returns_list():
    @generate(list)
    def generator_function():
        yield 1
        yield 2
        yield 3

    g = generator_function()
    assert isinstance(g, list)


def test_generate_tuple_returns_tuple():
    @generate(tuple)
    def generator_function():
        yield 1
        yield 2
        yield 3

    g = generator_function()
    assert isinstance(g, tuple)


def test_generate_list_returns_expected_items():
    @generate(list)
    def generator_function():
        yield 2
        yield 9
        yield 17

    g = generator_function()
    assert g == [2, 9, 17]
