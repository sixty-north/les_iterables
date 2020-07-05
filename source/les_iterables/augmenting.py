import itertools


def repeat_first(iterable):
    """Repeat the first item from an iterable on the end.

    Example:
        >>> ''.join(repeat_first("ABDC"))
        "ABCDA"

    Useful for making a closed cycle out of elements.
    If iterable is empty, the result will also be empty.

    Args:
        An iterable series of items.

    Yields:
        All items from iterables, followed by the first item from iterable.
    """
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return

    yield first

    for item in iterator:
        yield item

    yield first


def prepend(item, iterable):
    yield item
    yield from iterable


def prepend_if(item, iterable, condition):
    if condition:
        yield item
    yield from iterable


def append(iterable, item):
    yield from iterable
    yield item


def append_if(iterable, item, condition):
    yield from iterable
    if condition:
        yield item


def alternate_with(items, alternate_item):
    """Generate a series from items, alternating with an alternate item.

    items[0], alternate_item, items[1], alternate_item, ... ,items[n - 1], alternate_item
    """
    for item in items:
        yield item
        yield alternate_item


def ensure_contains(items, ensured_item):
    """Yield items, followed by ensured_item, if ensured_item is not already present.
    """
    present = False
    for item in items:
        present = present and (item == ensured_item)
        yield item

    if not present:
        yield ensured_item


def extend(iterable, item_factory=lambda: None):
    return itertools.chain(iterable, iter(item_factory, object()))