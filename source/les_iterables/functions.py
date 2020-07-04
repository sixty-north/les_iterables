from itertools import filterfalse


def retain_if(predicate, iterable):
    """Retain those items for which predicate evaluates to True.

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


def retain_falsey(iterable):
    """Retain those items which evaluate to True in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is True.
    """
    return filter(None, iterable)


def reject_truthy(iterable):
    """Reject those items which evaluate to True in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is False.
    """
    return retain_falsey(iterable)


def reject_falsey(iterable):
    """Reject those items which evaluate to False in a boolean context.

    Args:
        iterable: The iterable series of items to be filtered.

    Returns:
        An iterable series of items for which bool(item) is True.
    """
    return retain_truthy(iterable)
