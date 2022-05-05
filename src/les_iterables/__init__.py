from .version import __version__, __version_info__

from .augmenting import (
    repeat_first,
    prepend,
    prepend_if,
    append,
    append_if,
    alternate_with,
    separate_with,
    ensure_contains,
    extend,
)

from .generating import (
    one,
    generate,
)

from .grouping import (
    group_by_terminator,
    pairwise_padded,
    partition_tail,
    split_around,
)

from .parsing import (
    range_from_text,
    expand_numbered_list,
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
    take_before_exclusive,
    take_before_inclusive,
    take_until_exclusive,
    take_until_inclusive,
    take_between_inclusive,
    take_between_inclusive_values,
    transform_if,
    single,
    skip_while,
)

from .searching import (
    first_matching,
    nth_matching,
    duplicates,
)

from .sequences import (
    pop_n,
)

from .combining import (
    join_with
)

__all__ = [
    "alternate_with",
    "append",
    "append_if",
    "duplicates",
    "ensure_contains",
    "expand_numbered_list",
    "extend",
    "first_matching",
    "generate",
    "group_by_terminator",
    "join_with",
    "nth_matching",
    "one",
    "pairwise_padded",
    "partition_tail",
    "pop_n",
    "prepend",
    "prepend_if",
    "range_from_text",
    "reject_falsy",
    "reject_if",
    "reject_truthy",
    "repeat_first",
    "retain_falsy",
    "retain_if",
    "retain_truthy",
    "separate_with",
    "single",
    "skip_while",
    "split_around",
    "transform_if",
    "take_after_inclusive",
    "take_after_last_match",
    "take_before_exclusive",
    "take_before_inclusive",
    "take_until_exclusive",
    "take_until_inclusive",
    "take_between_inclusive",
    "take_between_inclusive_values",
]
