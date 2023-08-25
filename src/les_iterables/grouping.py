from collections import deque
from collections.abc import Sequence
from itertools import tee, zip_longest

from more_itertools import chunked


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
        To partition the last three items of an iterable series, do::

            head, tail = partition_tail(range(10), 3)
            for item in head:
                print(item)  # Prints all but the last three

            for item in tail:
                print(item)  # Prints the last three

    Raises:
        ValueError: If n is negative.
    """

    p = PartitionedTail(items, n)
    h = HeadPartitionIterator(p)
    t = TailPartitionIterator(p)
    return h, t


class PartitionedTail:

    def __init__(self, items, n):
        if n < 0:
            raise ValueError(f"Cannot partition negative number ({n}) items into the tail")

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
        self._pt._d.append(incoming_item)
        outgoing_item = self._pt._d.popleft()
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


def group_by_terminator(iterable, predicate, group_factory=None):
    """Group the items of an iterable series, starting a new group after each terminator.

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


def pairwise_padded(iterable, fillvalue=None):
    """Each item in an iterable series with its successor.

    The number of pairs returned will be equal to the number of items.

    Args:
        iterable: An iterable series of items to be grouped into pairs.
        fillvalue: The value used as the successor to the last item.

    Yields:
        A series of 2-tuples contain an item and its successor. For the last item
        the successor will be the fillvalue.
    """
    a, b = tee(iterable)
    next(b, fillvalue)
    return zip_longest(a, b, fillvalue=fillvalue)


def split_after_first(iterable, predicate, group_factory=None):
    """Split the iterable after the element matching the predicate.

    Always returns at least 1 group, and no more than 2 groups.
    If there is no element matching the predicate, the iterable is returned unchanged.
    If the iterable is empty, returns a single empty group.

    Examples:

        ::

            group, *groups = split_after_first([1, 2, 3, 1, 2, 3], lambda x: x == 2))
            assert group == [1, 2]
            assert groups == [[3, 1, 2, 3]]

            group, *groups = split_after_first([1, 2, 3], lambda x: x == 3)
            assert group == [1, 2, 3]
            assert groups == []

            group, *groups = split_after_first('abcde', lambda x: x == 'c')
            assert group ==  'abc'
            assert groups == ['de']

    Returns:
        An iterable series of groups.
    """
    group_factory = _make_group_factory(iterable, group_factory)
    group = []
    iterator = iter(iterable)
    for item in iterator:
        group.append(item)
        if predicate(item):
            break
    yield group_factory(group)
    remainder = list(iterator)
    if remainder:
        yield group_factory(remainder)


def partition(iterable, predicate, group_factory=None):
    group_factory = _make_group_factory(iterable, group_factory)

    before = []
    separator = []

    iterator = iter(iterable)
    for item in iterator:
        if not predicate(item):
            before.append(item)
        else:
            separator.append(item)
            break
    after = list(iterator)
    return (
        group_factory(before),
        group_factory(separator),
        group_factory(after),
    )


def _make_group_factory(iterable, group_factory=None):
    if group_factory is None:
        if isinstance(iterable, str):
            group_factory = lambda s: ''.join(s)
        elif isinstance(iterable, list):
            group_factory = lambda s: s
        elif isinstance(iterable, Sequence):
            group_factory = type(iterable)
        else:
            group_factory = lambda s: s
    return group_factory


def complete_chunks(iterable, n, group_factory=None):
    """Break an iterable series into chunks of a specified size. Incomplete chunks are discarded.

    Args:
        iterable: The iterable series to be chunked.
        n: The size of each chunk.
        group_factory: A callable which creates a group given a sequence of items.

    Yields:
        A series of groups of size n.
    """
    group_factory = _make_group_factory(iterable, group_factory)
    for chunk in chunked(iterable, n):
        if len(chunk) == n:
            yield group_factory(chunk)
