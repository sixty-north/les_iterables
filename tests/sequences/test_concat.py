from pytest import raises

from les_iterables.sequences import concat


def test_concate_no_args_raises_type_error():
    with raises(TypeError):
        concat()

def test_concat_single_empty_strings_returns_arg():
    assert concat("") == ""


def test_concat_two_empty_strings_returns_empty_string():
    assert concat("", "") == ""


def test_concat_one_string():
    assert concat("norway") == "norway"


def test_concat_two_strings():
    assert concat("un", "believable") == "unbelievable"


def test_concat_three_strings():
    assert concat("new", "found", "land") == "newfoundland"


def test_concat_empty_list_returns_arg():
    assert concat([]) == []


def test_concat_two_empty_lists_returns_empty_list():
    assert concat([], []) == []


def test_concat_one_list():
    assert concat([4, 7, 2]) == [4, 7, 2]


def test_concat_two_lists():
    assert (
        concat([2, 4, 6, 8], ["who", "do", "we", "appreciate"])
        ==
        [2, 4, 6, 8, "who", "do", "we", "appreciate"]
    )

def test_concat_empty_tuple_returns_arg():
    assert concat(tuple()) == tuple()


def test_concat_two_empty_tuples_returns_empty_list():
    assert concat(tuple(), tuple()) == tuple()


def test_concat_one_tuple():
    assert concat((4, 7, 2)) == (4, 7, 2)


def test_concat_two_tuples():
    assert (
        concat((2, 4, 6, 8), ("who", "do", "we", "appreciate"))
        ==
        (2, 4, 6, 8, "who", "do", "we", "appreciate")
    )


def test_concat_list_and_tuple_gives_list():
    assert (
        concat([2, 4, 6, 8], ("who", "do", "we", "appreciate"))
        ==
        [2, 4, 6, 8, "who", "do", "we", "appreciate"]
    )


def test_concat_tuple_and_list_gives_tuple():
    assert (
        concat([2, 4, 6, 8], ("who", "do", "we", "appreciate"))
        ==
        [2, 4, 6, 8, "who", "do", "we", "appreciate"]
    )


def test_concat_str_and_list_gives_tuple():
    with raises(TypeError):
        concat("chant", ("who", "do", "we", "appreciate"))
