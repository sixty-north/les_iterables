import functools


def one(item):
    """Yield an iterable series of one item.

    Args:
        item: The item to be yielded.

    Yields:
        An iterable series of a single item.
    """
    yield item


def generate(collection=None):
    """A decorator factory to make a generator return a fully realised collection.

    Some functions are easier to write as generator functions, even though we don't want the
    lazy behaviour of generators. Use this decorator to fully consume a generator into a collection.

    Args:
        collection: The collection type to be realised. The default of nothing causes
            this decorator to do nothing. Normall a collection type such as a list, set
            or tuple is provided.

    Returns:
        A decorator function which decorates a function with a wrapper which fully evaluates
        the wrapped generator function, and uses it to create a collection.
    """

    if collection is None:
        collection = lambda x: x

    def eager(f):

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return collection(f(*args, **kwargs))

        return wrapper

    return eager
