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


def true(*args, **kwargs):
    return True


def false(*args, **kwargs):
    return False

