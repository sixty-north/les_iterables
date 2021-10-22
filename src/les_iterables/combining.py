"""Functions for combining iterable series.
"""

def join_with(items, separators):
    """Generate a series of items, with separators taken from a second series.

    The number of separators consumed will be one fewer than the number of items.

    items[0], separators[0], items[1], separators[1], ..., separators[n-2], items[n-1]

    Args:
        items: An iterable series of items to return.
        separators: A series of items one of which will be returned between each item. The number
            of available separators must be at least one less than the number of items. Separators
            will only be consumed as required.

    Returns:
        The series of items alternating with items from separators. The first value yielded
        will be the first item. The last value yielded will be the last item. If items is empty
        an empty series will be yielded.

    Raises:
         ValueError: If there are too few separators to go between the supplied number of
            items.
    """
    item_iterator = iter(items)
    try:
        item = next(item_iterator)
    except StopIteration:
        return
    yield item

    separator_iterator = iter(separators)

    for item in item_iterator:
        try:
            separator = next(separator_iterator)
        except StopIteration:
            raise ValueError("Too few separators to join_with items")
        yield separator
        yield item
