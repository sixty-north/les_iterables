import functools
import itertools
from collections import deque

from les_iterables.augmenting import extend


def just(item):
    """An iterable of just one item.

    Args:
        item: The item to be yielded.

    Yields:
        The item.
    """
    yield item


def range_from_text(text_range):
    """A range of integers from a textual description.

    Args:
        text_range: A string of the form "<first>-<last>" such as "7-10" describing the inclusive
            ends of a range of integers.

    Returns:
        A range object.
    """
    first, separator, last = text_range.partition("-")
    start = int(first)
    last = int(last)
    stop = last + 1 if separator else start + 1
    if stop < start:
        raise ValueError(f"Textual range {text_range} has start {start} after last {last}")
    return range(start, stop)


def expand_numbered_list(indexes):
    """Expands a string containing numbered items into a list of integers.

    e.g. "1, 2, 5, 7-10, 15, 20-25" -> [1, 2, 5, 7, 8, 9, 10, 15, 20, 21, 22, 23, 24, 25]
    """
    text_ranges = indexes.split(",")
    ranges = map(range_from_text, text_ranges)
    return list(itertools.chain.from_iterable(ranges))


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

    Example:
        split_around("abc\ndef\n", is_newline) -> ['a', 'b', 'c'], ['\n'], ['\n'], ['d', 'e', 'f']

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


def partition_tail(items, n):
    """Lazily partition an iterable series into a head, and tail of no more than specified length.

    Args:
         items: An iterable series of items.
         n: The maximum number of items to be partitioned into the tail.

    Returns:
        A pair of iterators, head and tail. Consuming any items from the tail iterator will cause
        the entire head iterator to be consumed, so typically the head iterator should be consumed
        before consuming any items from the tail iterator.

    Example:

         head, tail = partition_tail(range(10), 3)
         for item in head:
             print(item)  # Prints all but the last three

         for item in tail:
             print(item)  # Prints the last three
    """

    p = PartitionedTail(items, n)
    h = HeadPartitionIterator(p)
    t = TailPartitionIterator(p)
    return h, t


class PartitionedTail:

    def __init__(self, items, n):
        self._i = iter(items)
        self._n = n
        self._d = deque()
        self._head_iterator = None
        self._tail_iterator = None


class HeadPartitionIterator:

    def __init__(self, partition_tail):
        self._pt = partition_tail
        self._pt._head_iterator = self

    def __iter__(self):
        return self

    def __next__(self):
        while len(self._pt._d) < self._pt._n:
            self._pt._d.append(next(self._pt._i))

        assert len(self._pt._d) == self._pt._n
        incoming_item = next(self._pt._i)  # If this raises StopIteration, allow it to propagate
        outgoing_item = self._pt._d.popleft()
        self._pt._d.append(incoming_item)
        assert len(self._pt._d) == self._pt._n
        return outgoing_item


class TailPartitionIterator:

    def __init__(self, partition_tail):
        self._pt = partition_tail
        self._pt._tail_iterator = self
        self._consumed_head = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self._consumed_head:
            deque(self._pt._head_iterator, maxlen=0)  # Consume all items
            self._consumed_head = True
        if len(self._pt._d) == 0:
            raise StopIteration
        return self._pt._d.popleft()


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