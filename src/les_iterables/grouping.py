from collections import deque


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
