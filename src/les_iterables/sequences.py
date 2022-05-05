from collections import deque


def pop_n(sequence, n, factory=None):
    """Remove n items from the end of a sequence.

    Args:
        sequence: The sequence from which to remove items.

        n: The number of items to remove.

        factory: The sequence return type. By default will be the same
            as the input type.

    Return:
        A sequence containing the removed items in the same order
        they were in the original sequence.

    Raises:
        IndexError: If there are fewer than n items in the sequence.
    """
    factory = factory or type(sequence)
    items = deque()
    for i in range(n):
        items.appendleft(sequence.pop())
    return items if isinstance(items, factory) else factory(items)
