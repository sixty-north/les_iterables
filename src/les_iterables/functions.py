import functools
import itertools

from les_iterables.augmenting import extend


def just(item):
    """An iterable of just one item.

    Args:
        item: The item to be yielded.

    Yields:
        The item.
    """
    yield item


def generate(collection=None):

    if collection is None:
        collection = lambda x: x

    def eager(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return collection(f(*args, **kwargs))

        return wrapper

    return eager


def pairwise_padded(iterable, fillvalue=None):
    a, b = itertools.tee(iterable)
    next(b, fillvalue)
    return itertools.zip_longest(a, b, fillvalue=fillvalue)


def transform_if(iterable, predicate, transform):
    for item in iterable:
        yield transform(item) if predicate(item) else item


def group_by_terminator(iterable, predicate, group_factory=None):
    """Group the items of of an iterable series, starting a new group after each terminator.

    Each group will have as it's last item an item from which the predicate returns True. For all
    preceding items in the group the predicate will return False.  The last group yielded may be
    incomplete, without a terminator.

    Args:
        iterable: An iterable series of items to be grouped.

        predicate: A unary callable function used to detect group-terminating items from the
            iterable series.

        group_factory: A callable which creates a group given an sequence of items. By default,
            a list.

    Yields:
        A series of groups.
    """
    if group_factory is None:
        group_factory = lambda x: x
    group = []
    for item in iterable:
        group.append(item)
        if predicate(item):
            yield group_factory(group)
            group = []
    if group:
        yield group_factory(group)


def split_around(iterable, predicate, group_factory=None):
    """Split an iterable series into groups around specific items.

    Each item for which the predicate returns True will be in its own group.

    Args:
        iterable: An iterable series of items to be grouped.

        predicate: A unary callable to detect items which should be placed in their own group.

        group_factory: A callable which creates a group given a sequence of items. By default, a
            list.

    Yields:
        A series of groups.
    """
    if group_factory is None:
        group_factory = lambda x: x
    group = []
    for item in iterable:
        if predicate(item):
            if group:
                yield group_factory(group)
                group = []
            group.append(item)
            yield group_factory(group)
            group = []
        else:
            group.append(item)
    if group:
        yield group_factory(group)


def elements_at(seq, indexes):
    """Select elements from a sequence based on their indexes.

    Args:
        seq: The sequence from which to select elements.

        indexes: Indexes into seq indicating the selected elements.

    Yields:
        A series of items selected from seq by indexes.

    Raises:
        IndexError: If one of the indexes is not valid with seq.
    """
    for index in indexes:
        yield seq[index]


def indexes(seq, item):
    """The indexes at which item occurs in a sequence.

    Args:
        seq: A sequence in which to search for occurrences of item.
        item: The item for which to determine indexes.

    Yields:
        A series of indexes into seq at which item occurs.
    """
    i = 0
    while True:
        try:
            i = seq.index(item, i)
        except ValueError:
            break
        yield i
        i += 1


def unchain(iterable, box=None):
    if box is None:
        box = lambda item: [item]
    return itertools.chain(map(box, iterable))


def extended_unchain(iterable, box=list):
    """Convert an iterable into an infinite series of lists of containing zero or one items.
    """
    return extend(unchain(iterable, box), box)


def empty_iterable():
    yield from ()


def run_length_encode(items):
    return ((key, len(list(group))) for key, group in itertools.groupby(items))


def false_then_true():
    """A single False value followed by True values.
    """
    yield False
    while True:
        yield True


def true_then_false():
    """A single True value followed by False values.
    """
    yield True
    while True:
        yield False