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
    """Yield an item followed by an iterable.
    """
    yield item
    yield from iterable


def prepend_if(item, iterable, condition):
    """Conditionally yield an item, followed by an iterable.
    """
    if condition:
        yield item
    yield from iterable


def append(iterable, item):
    """Yield an iterable followed by an item.
    """
    yield from iterable
    yield item


def append_if(iterable, item, condition):
    """Yield an iterable, conditionally followed by an item.
    """
    yield from iterable
    if condition:
        yield item


def alternate_with(items, alternate_item):
    """Generate a series from items, alternating with an alternate item.

    items[0], alternate_item, items[1], alternate_item, ... ,items[n - 1], alternate_item

    The last item yielded will be alternate_item
    """
    for item in items:
        yield item
        yield alternate_item


def separate_with(items, separator):
    """Generate a series from items, where the original items are separated by another item.

    items[0], separator, items[1], separator, items[2] ... separator, items[n]

    The last item yielded will be the last element of items.
    """
    iterator = iter(items)
    try:
        item = next(iterator)
    except StopIteration:
        return

    yield item

    for item in iterator:
        yield separator
        yield item


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
    """Extend an iterable by yielding items returned by a factory.

    Args:
         iterable: An iterable series of items to be extended.

         items_factory: A zero-argument callable that will be invoked once
            for reach item requested beyond the end of iterator to create
            additional items as necessary.
    """
    return itertools.chain(iterable, iter(item_factory, object()))
