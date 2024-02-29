from itertools import filterfalse, tee

from more_itertools import stagger

from les_iterables.sentinels import MISSING


def single(iterable):
    i = iter(iterable)
    try:
        item = next(i)
    except StopIteration:
        raise ValueError("Too few items")

    try:
        next(i)
    except StopIteration:
        return item
    raise ValueError("Too many items")


def element_at(iterable, index, *, start=0):
    for i, item in enumerate(iterable, start):
        if i == index:
            return i
    raise IndexError("No element at index {i} with given start index {start}")


def retain_if(predicate, iterable):
    """Retain those items for which predicate evaluates to True.

    Example:

        >>> list(retain_if(lambda x: x%2 == 0, range(10)))
        [0, 2, 4, 6, 8]

    Args:
        predicate: A single-argument callable to which each item of iterable
            will be passed in turn to determine whether it should be retained,
            by returning True, or rejected, by returning False.

        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which predicate returns True.
    """
    if not callable(predicate):
        raise TypeError(f"predicate {predicate} is not callable")
    return filter(predicate, iterable)


def reject_if(predicate, iterable):
    """Retain those items for which predicate evaluates to True.

    Example:

        >>> list(reject_if(lambda x: x%2 == 0, range(10)))
        [1, 3, 5, 7, 9]

    Args:
        predicate: A single-argument callable to which each item of iterable
            will be passed in turn to determine whether it should be rejected,
            by returning True, or retained, by returning False.

        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which predicate returns False.
    """
    if not callable(predicate):
        raise TypeError(f"predicate {predicate} is not callable")
    return filterfalse(predicate, iterable)


def reject_if_none(iterable):
    """Reject those items which are None.

    Example:

        >>> list(reject_if_none(, [1, 3, None, 7, None]))
        [1, 3, 7]

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items without None values.
    """
    return reject_if(lambda item: item is None, iterable)


def retain_if_not_none(iterable):
    """Retain those items which are not None.

    Example:

        >>> list(retain_if_not_none(, [1, 3, None, 7, None]))
        [1, 3, 7]

    Returns:
        An iterable series of items without None values.
    """
    return retain_if(lambda item: item is not None, iterable)


def retain_truthy(iterable):
    """Retain those items which evaluate to True in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is True.
    """
    return filter(None, iterable)


def retain_falsy(iterable):
    """Retain those items which evaluate to False in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is True.
    """
    return filterfalse(None, iterable)


def reject_truthy(iterable):
    """Reject those items which evaluate to True in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is False.
    """
    return retain_falsy(iterable)


def reject_falsy(iterable):
    """Reject those items which evaluate to False in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is True.
    """
    return retain_truthy(iterable)


def take_after_last_match(iterable, predicate):
    """Yield items in an iterable series after the last matching.

    Warning:
        This function potentially allocates sufficient space to store
        the entire series.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select items.

    Returns:
        A sequence containing the tail of the iterable series after the last match.
    """
    # TODO: What is the required behaviour if there is no match?
    tail = []
    for item in iterable:
        if predicate(item):
            tail.clear()
        else:
            tail.append(item)
    return tail


def take_after_inclusive(iterable, predicate):
    """Yield items starting with the first match.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select the first item.

    Yields:
        Items starting with the first match.
    """
    found = False
    for item in iterable:
        found = found or predicate(item)
        if found:
            yield item


def take_after_exclusive(iterable, predicate):
    """Yield items in an iterable series after the first matching.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select items.
    """
    found = False
    for item in iterable:
        if found:
            yield item
        else:
            found = predicate(item)


def take_before_inclusive(iterable, predicate):
    """Yield items up to and including the first match.

    If no matching item is present, the result is empty.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select the last item.

    Returns:
        A sequence of items finishing with the first match.
    """
    items = []
    for item in iterable:
        items.append(item)
        if predicate(item):
            return items
    return []


def take_before_exclusive(iterable, predicate):
    """Yield items up to but excluding including the first match.

    If no matching item is present, the result is empty.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select the last item.

    Returns:
        A sequence of items finishing with the first match.
    """
    items = []
    for item in iterable:
        if predicate(item):
            return items
        items.append(item)
    return []



def take_until_inclusive(iterable, predicate):
    """Yield items up and including the first match.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select item after the last item.

    Returns:
        A series of items finishing with but excluding the first match.
    """
    for item in iterable:
        yield item
        if predicate(item):
            return


def take_until_exclusive(iterable, predicate):
    """Yield items up to but excluding the first match.

    Args:
        iterable: An iterable series of items.

        predicate: A function of one argument used to select item after the last item.

    Returns:
        A series of items finishing with but excluding the first match.
    """
    for item in iterable:
        if predicate(item):
            return
        yield item


def take_between_inclusive(iterable, first_predicate, last_predicate):
    """A list of items from the first matching to the last matching inclusive.

    Args:
        iterable: An iterable series of items.

        first_predicate: A function of one argument used to select the first item in
            the result.

        last_predicate: A function of one argument used to select the last item in
            the result.

        Returns:
             Either a sequence of at least two elements, or an empty sequence if elements
             matching the first predicate and the last predicate were not both found.
    """
    return take_before_inclusive(take_after_inclusive(iterable, first_predicate), last_predicate)


def take_between_inclusive_values(iterable, first, last):
    """A list of items from the first matching to the last matching inclusive.

    Args:
        iterable: An iterable series of items.

        first: A value marking the start of the result sequence.

        last: A value marking the end of the result sequence.

        Returns:
             Either a sequence of at least two elements, or an empty sequence if elements
             matching the first predicate and the last predicate were not both found.
    """
    return take_between_inclusive(iterable, lambda item: item == first, lambda item: item == last)


def take_between_exclusive(iterable, first_predicate, last_predicate):
    """A list of items from the first matching to the last matching exclusive.

    Args:
        iterable: An iterable series of items.

        first_predicate: A function of one argument used to select the first item before
            the result.

        last_predicate: A function of one argument used to select the first item after
            the result.

        Returns:
             A sequence of items between the first matching and the last matching. If either
                the first or last matching is not found, the result will be empty.
    """
    return take_before_exclusive(take_after_exclusive(iterable, first_predicate), last_predicate)


def take_between_exclusive_values(iterable, first, last):
    """A list of items from the first matching to the last matching exclusive.

    Args:
        iterable: An iterable series of items.

        first: A value marking the start of the result sequence.

        last: A value marking the end of the result sequence.

        Returns:
             A sequence of items between the first matching and the last matching. If either
                the first or last matching is not found, the result will be empty.
    """
    return take_between_exclusive(iterable, lambda item: item == first, lambda item: item == last)


def preceding(iterable, item):
    """The item which comes in the series immediately before the specified item.

    Args:
        iterable: The iterable series in which to search for item.
        item: The item to search for in iterable.

    Returns:
        The previous item.

    Raises:
        ValueError: If item is not present in iterable beyond the first item.
    """
    iterator = iter(iterable)
    try:
        current = next(iterator)
        if current == item:
            raise ValueError(f"No item preceding {item!r} in iterable series")
    except StopIteration:
        raise ValueError("Iterable series is empty")

    previous = current
    for current in iterator:
        if current == item:
            return previous
        previous = current
    raise ValueError(f"No item {item!r} in iterable series for which to return the preceding item")


def succeeding(iterable, item):
    """The item which comes in the series immediately after the specified item.

    Args:
        iterable: The iterable series in which to search for item.
        item: The item to search for in iterable.

    Returns:
        The next item.

    Raises:
        ValueError: If the item is not present before the penultimate item.
    """
    iterator = iter(iterable)
    for current in iterator:
        if current == item:
            break
    else:  # nobreak
        raise ValueError(
            f"No item {item!r} in iterable series for which to return the succeeding item"
        )
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError(f"No item succeeding {item!r} in iterable series")


def relative_to(iterable, item, *, offset, n=0, default=MISSING):
    """Return the item relative to the nth occurrence of some existing item.

    Args:
        iterable: The iterable series from which to search for item.
        item: The value to relative to which the returned item should be.
        offset: The positive or negative offset relative to the found item.
        n: Where it is the nth occurrence of item which will be searched for.
        default: The default value to return if not found.

    Returns:
        The item at a given offset from a specific value, or the default value if given.

    Raises:
        ValueError: If there is not item matching the criteria an no default
            value has been specified.
    """
    count = 0
    for p, q in stagger(iterable, (0, offset), longest=True, fillvalue=MISSING):
        if p == item:
            if count == n:
                if q is MISSING:
                    if default is MISSING:
                        raise ValueError
                    return default
                return q
            count += 1
    if default is MISSING:
        raise ValueError
    return default


def offset_iterators(iterable, offset: int):
    """Produce two iterators which are offset from each other by a given number of items.

    Once offset_iterators() has been called, and if the original itererable is an iterator
    (as opposed to a iterablecollection), the iterator should not be used anywhere else; otherwise,
    the iterator could get advanced without the offset_iterators objects being informed.

    The produced iterators will start with the requested offset but are independent and can be
    advanced independently. To keep them synchronized, consider iterating over them in lockstep
    using zip().

    Note that::

        p, q = offset_iterators(iterable, 0)

    is equivalent to::

        p, q = itertools.tee(iterable)

    Args:
        iterable: An iterable from which to return two iterators separated by offset.
        offset: An integer offset by which the two iterators should be separated. This offset can
            be positive or negative.

    Returns:
        Two iterators, the second of which will be offset from the first by the specified number
        (positive, negative or zero) places.

    Raises:
        ValueError: If the iterable is not long enough to accommodate two iterators separated
            by the specified offset.
    """
    p, q = tee(iterable)
    i = 0
    try:
        if offset > 0:
            for i in range(offset):
                next(q)
        if offset < 0:
            for i in range(-offset):
                next(p)
    except StopIteration:
        raise ValueError(f"Too few items ({i}) in iterable for iterators offset by {offset} places")
    return p, q


def skip_while(iterable, predicate):
    """Skip leading items while the predicate matches.

    Args:
        iterable: An iterable of items.
        predicate: A predicate function with which to test items.

    Yields:
        Those items including and after the first which doesn't match the predicate.
    """
    iterator = iter(iterable)
    for item in iterator:
        if not predicate(item):
            yield item
            break
    yield from iterator


def transform_if(iterable, predicate, transform):
    """Apply a transformation to items which match a predicate.

    Non-matching items will not be transformed.

    Args:
        iterable: An iterable of items.
        predicate: predicate: A predicate function with which to select items to be transformed.
        transform: A unary function which accepts an item to be transformed and returns the
            transformed item.

    Yields:
        An iterable series of items.
    """
    for item in iterable:
        yield transform(item) if predicate(item) else item
