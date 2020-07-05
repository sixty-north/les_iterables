# ![Les Itérables](docs/source/_static/les_iterables.png)

[![Documentation Status](https://readthedocs.org/projects/les-iterables/badge/?version=latest)](https://les-iterables.readthedocs.io/en/latest/?badge=latest)
      

## Installation

    $ pip install les_iterables


## Tests

Nope. Possibly this is simple enough that there are obviously no errors. I'll doubtless be proven wrong.

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

LOL.

To release, there is a short manual process:

    $ bumpversion patch
    $ python setup.py sdist bdist_wheel
    $ twine upload dist/* --config-file=path/to/sixty-north.pypirc