# ![Les Itérables](docs/source/_static/les_iterables.png)

[![Documentation Status](https://readthedocs.org/projects/les-iterables/badge/?version=latest)](https://les-iterables.readthedocs.io/en/latest/?badge=latest)

![CI](https://github.com/sixty-north/les_iterables/actions/workflows/actions.yml/badge.svg)


[![codecov](https://codecov.io/gh/sixty-north/les_iterables/branch/master/graph/badge.svg?token=66QU3UW6N3)](https://codecov.io/gh/sixty-north/les_iterables)

## Installation

    $ pip install les_iterables


## Examples

A collection of utility functions for processing iterable series which
aren't in [itertools](https://docs.python.org/3/library/itertools.html) or [more-itertools](https://more-itertools.readthedocs.io). Some are little more than simple aliases with less confusing names.

    >>> from les_iterables import *
    >>> is_odd = lambda x: x%2 != 0
    >>>
    >>> list(retain_if(is_odd, range(10))
    [1, 3, 5, 7, 9]
    >>>
    >>> list(reject_if(is_odd, range(10))
    [0, 2, 4, 6, 8]
    >>>
    >>> list(retain_truthy(reject_if(is_odd, range(10)))
    [2, 4, 6, 8]

## CI/CD

    $ bumpversion patch
    $ git push --follow-tags