from les_iterables import retain_if
from les_iterables.selecting import element_at


def nth_matching(iterable, predicate, index):
    return element_at(retain_if(iterable, predicate), index)


def first_matching(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("No matching items")
