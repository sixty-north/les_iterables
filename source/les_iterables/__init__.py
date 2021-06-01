from .version import __version__

from .augmenting import (
    repeat_first,
    prepend,
    prepend_if,
    append,
    append_if,
    alternate_with,
    ensure_contains,
    extend,
)


from .selecting import (
    retain_if,
    reject_if,
    retain_truthy,
    retain_falsy,
    reject_truthy,
    reject_falsy,
    take_after_last_match,
    take_after_inclusive,
    take_before_inclusive,
    take_between_inclusive,
    take_between_inclusive_values,
)

from .searching import (
    first_matching,
    nth_matching,
)

from .combining import (
    join_with
)

__all__ = [
    "__version__",
    "repeat_first",
    "prepend",
    "prepend_if",
    "append",
    "append_if",
    "alternate_with",
    "ensure_contains",
    "extend",
    "retain_if",
    "reject_if",
    "retain_truthy",
    "retain_falsy",
    "reject_truthy",
    "reject_falsy",
    "take_after_last_match",
    "take_after_inclusive",
    "take_before_inclusive",
    "take_between_inclusive",
    "take_between_inclusive_values",
    "first_matching",
    "nth_matching",
    "join_with",
]
