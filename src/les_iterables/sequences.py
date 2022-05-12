import itertools
from collections import deque
from typing import Union


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