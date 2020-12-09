from itertools import filterfalse


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
        This function potentially alloctates sufficient space to store
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


def take_before_inclusive(iterable, predicate):
    """Yield items up to and including the first match.

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

        last_predicate: A value marking the end of the result sequence.

        Returns:
             Either a sequence of at least two elements, or an empty sequence if elements
             matching the first predicate and the last predicate were not both found.
    """
    return take_between_inclusive(iterable, lambda item: item == first, lambda item: item == last)
