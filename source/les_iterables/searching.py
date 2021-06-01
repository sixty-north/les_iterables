from les_iterables import retain_if
from les_iterables.selecting import element_at


def nth_matching(iterable, predicate, n):
    """The nth item matching a predicate.

    Args:
        iterable: An iterable series of items to be searched.
        predicate: A callable to which each item will be passed in turn.
        n: A zero-based index.

    Returns:
        The nth item for which the predicate returns True.

    Raises:
        ValueError: If there are no matching items.
    """
    return element_at(retain_if(iterable, predicate), n)


def first_matching(iterable, predicate):
    """The first item matching a predicate.

    Args:
        iterable: An iterable series of items to be searched.
        predicate: A callable to which each item will be passed in turn.

    Returns:
        The first item for which the predicate returns True.

    Raises:
        ValueError: If there are no matching items.
    """
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("No matching items")
