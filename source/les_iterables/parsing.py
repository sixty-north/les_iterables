import itertools
from functools import partial


def range_from_text(text_range: str, separator="-") -> range:
    """A range of integers from a textual description.

    Args:
        text_range: A string of the form "<first>-<last>" such as "7-10" describing the inclusive
            ends of a range of integers.

    Returns:
        A range object.

    Raises:
        ValueError: If the string could not be parsed as an ascending range of at least one item.
    """
    if not (0 <= text_range.count(separator) <= 1):
        raise ValueError(f"Could not parse range {text_range!r}. Only positive integers are supported.")
    first, sep, last = text_range.partition(separator)
    start = int(first)
    last = last and int(last)
    stop = last + 1 if sep else start + 1
    if stop < start:
        raise ValueError(f"Textual range {text_range} has start {start} after last {last}")
    return range(start, stop)


def expand_numbered_list(text, *, separator=",", range_separator="-"):
    """Expands a string containing numbered items into a list of integers.

    e.g. "1, 2, 5, 7-10, 15, 20-25" -> [1, 2, 5, 7, 8, 9, 10, 15, 20, 21, 22, 23, 24, 25]

    Args:
        text: A string containing separated integers and ascending integer ranges.
        separator: The item separator. Defaults to ",".
        range_separator: The separator between the beginning and end of a range.
            Defaults to "-"

    Yields:
        An iterable series of integers.

    Raises:
        ValueError: If the list could not be parsed.
    """
    text_ranges = text.split(separator)
    ranges = map(partial(range_from_text, separator=range_separator), text_ranges)
    return itertools.chain.from_iterable(ranges)