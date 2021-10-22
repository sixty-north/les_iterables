from collections import defaultdict

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


def duplicates(iterable, key=None):
    """Find duplicate items.

      [1, 3, 6, 3, 6, 2, 9, 3] -> [3, 6, 3]

    Args:
        iterable: The items to be searched.

        key: An optional function used to generate a key by which items will be compared. If not
            provided the items themselves will be compared. If the key function returns hashable
            objects the performance of this function will be O(n); however, the performance will
            degrade to O(n²) when the first non-hashable key is encountered.

    Yields:
         Items which are considered duplicates according to the key, in the order that they are
         encountered. Items which are encountered more than twice will be yielded more than once.
    """
    if key is None:
        key = lambda x: x
    seen_keys = set()
    appender = set.add
    for item in iterable:
        k = key(item)
        try:
            seen = k in seen_keys # O(1) to O(n)
        except TypeError:
            # k is unhashable, so switch strategy by converting seen_keys from a set to a list
            seen_keys = list(seen_keys)
            appender = list.append
            seen = False
        if seen:
            yield item
        appender(seen_keys, k)
