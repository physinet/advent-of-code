from operator import and_
from functools import reduce
from helpers import get_input


def _item_in_both_compartments(row: str) -> str:
    i = len(row) // 2
    c1, c2 = row[:i], row[i:]
    (item,) = set(c1) & set(c2)
    return item


def _priority(item: str) -> int:
    if item.isupper():
        return ord(item) - 65 + 27
    return ord(item) - 96


def sum_priorities(rows: list[str]) -> int:
    return sum(_priority(_item_in_both_compartments(row)) for row in rows)


def _item_in_all_groups(rows: list[str]) -> str:
    sets = map(set, map(str.strip, rows))
    (item,) = reduce(and_, sets)
    return item


def sum_priorities_part2(rows) -> int:
    return sum(
        _priority(_item_in_all_groups(rows[i : i + 3])) for i in range(0, len(rows), 3)
    )


TEST = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

if __name__ == "__main__":
    assert sum_priorities(TEST) == 157
    print(sum_priorities(get_input(3)))
    assert sum_priorities_part2(TEST) == 70
    print(sum_priorities_part2(get_input(3)))
