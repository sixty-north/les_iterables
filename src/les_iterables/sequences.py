import itertools
from collections import deque
from typing import Union

from les_iterables.functions import false


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
    if n < 0:
        raise ValueError(f"Cannot pop {n} items from sequence")
    factory = factory or type(sequence)
    items = deque()
    for i in range(n):
        items.appendleft(sequence.pop())
    return items if isinstance(items, factory) else factory(items)


def concat(sequence, *sequences):
    """Concatenate one of more sequences of compatible types.

    Args:
        sequence: A sequence.
        *sequences: Additional sequences to concatenate with the first.

    Returns:
        A concatenated sequences which has the same type as the first sequence.

    Raises:
        TypeError: If the sequences are not of compatible types.
    """

    if len(sequences) == 0:
        return sequence

    sequences = (sequence, *sequences)

    if all(isinstance(s, str) for s in sequences):
        return "".join(sequences)
    sequence_type = type(sequences[0])
    if issubclass(sequence_type, str):
        raise TypeError(f"Cannot concatenate str with non-string type {type(sequences[1]).__name__}")
    return sequence_type(itertools.chain.from_iterable(sequences))


def replace_range(s, r: Union[range, slice], t):
    """Replace the elements of s in a range with a new sequence.

    Args:
        s: The string in which a range is to be replaced.
        r: A range or slice of indexes in s to be replaced.
        t: The sequence with which to replace the elements of s in the range.

    Returns:
        The sequence with the elements specified by a range of indexes replaced.
    """
    if hasattr(r, "step") and r.step not in {1, None}:
        raise ValueError(f"Cannot replace range specified by {type(r).__name__} with step {r.step} not equal to 1")
    prefix = s[:r.start]
    suffix = s[r.stop:]
    return concat(prefix, t, suffix)


def append_unique(sequence, item) -> bool:
    """Append an item to a sequence if it is not already present.

    Args:
        sequence: The sequence to which the item is to be appended.
        item: The item to be appended.

    Returns:
        True if the item was appended, False if it was already present.
    """
    if item not in sequence:
        sequence.append(item)
        return True
    return False


def prepend_unique(sequence, item) -> bool:
    """Prepend an item to a sequence if it is not already present.

    Args:
        sequence: The sequence to which the item is to be prepended.
        item: The item to be prepended.

    Returns:
        True if the item was prepended, False if it was already present.
    """
    if item not in sequence:
        sequence.insert(0, item)
        return True
    return False


def insert_unique(sequence, index, item) -> bool:
    """Insert an item into a sequence if it is not already present.

    Args:
        sequence: The sequence into which the item is to be inserted.
        index: The index at which the item is to be inserted.
        item: The item to be inserted.

    Returns:
        True if the item was inserted, False if it was already present.
    """
    if item not in sequence:
        sequence.insert(index, item)
        return True
    return False


def extend_unique(sequence, items) -> set:
    """Extend a sequence with items which are not already present.

    Args:
        sequence: The sequence to which the items are to be appended.
        items: The items to be appended.

    Returns:
        A set of the items which were appended.
    """
    existing = set(sequence)
    added = set()
    for item in items:
        if item not in existing and item not in added:
            sequence.append(item)
            added.add(item)
    return added
