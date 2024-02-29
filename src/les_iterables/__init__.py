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
    complete_chunks,
    group_by_terminator,
    pairwise_padded,
    partition,
    partition_tail,
    split_around,
    split_after_first,
)

from .parsing import (
    range_from_text,
    expand_numbered_list,
)


from .selecting import (
    retain_if,
    retain_if_not_none,
    reject_if,
    reject_if_none,
    retain_truthy,
    retain_falsy,
    reject_truthy,
    reject_falsy,
    take_after_last_match,
    take_after_exclusive,
    take_after_inclusive,
    take_before_exclusive,
    take_before_inclusive,
    take_until_exclusive,
    take_until_inclusive,
    take_between_exclusive,
    take_between_exclusive_values,
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
    run_delimited_range,
)

from .sequences import (
    concat,
    pop_n,
    replace_range,
    append_unique,
    prepend_unique,
    insert_unique,
    extend_unique,
)

from .combining import (
    join_with,
    flatten,
)

__all__ = [
    "alternate_with",
    "append",
    "append_if",
    "append_unique",
    "complete_chunks",
    "concat",
    "duplicates",
    "ensure_contains",
    "expand_numbered_list",
    "extend",
    "extend_unique",
    "first_matching",
    "flatten",
    "generate",
    "group_by_terminator",
    "insert_unique",
    "join_with",
    "nth_matching",
    "one",
    "pairwise_padded",
    "partition",
    "partition_tail",
    "pop_n",
    "prepend",
    "prepend_if",
    "prepend_unique",
    "range_from_text",
    "reject_falsy",
    "reject_if",
    "reject_if_none",
    "reject_truthy",
    "repeat_first",
    "replace_range",
    "retain_falsy",
    "retain_if",
    "retain_if_not_none",
    "retain_truthy",
    "run_delimited_range",
    "separate_with",
    "single",
    "skip_while",
    "split_around",
    "split_after_first",
    "transform_if",
    "take_after_inclusive",
    "take_after_last_match",
    "take_before_exclusive",
    "take_before_inclusive",
    "take_until_exclusive",
    "take_until_inclusive",
    "take_between_exclusive",
    "take_between_exclusive_values",
    "take_between_inclusive",
    "take_between_inclusive_values",
]
