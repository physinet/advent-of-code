import re
from typing import Callable

from dataclasses import dataclass

from helpers import get_input

TEST = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    divisible_by: int
    true_target: int
    false_target: int
    num_inspections: int = 0


def _parse_operation(operation):
    return lambda old: eval(operation)


def parse_input(rows):
    monkeys = {}
    for row in rows:
        row = row.strip()
        if regex_match := re.match("^Monkey (\d+):$", row):
            monkey_id = int(regex_match.group(1))
        elif regex_match := re.match("^Starting items: (.*)$", row):
            items = [int(x) for x in regex_match.group(1).split(",")]
        elif regex_match := re.match("^Operation: new = (.*)$", row):
            operation = _parse_operation(regex_match.group(1))
        elif regex_match := re.match("^Test: divisible by (\d+)$", row):
            divisible_by = int(regex_match.group(1))
        elif regex_match := re.match("^If true: throw to monkey (\d+)$", row):
            true_target = int(regex_match.group(1))
        elif regex_match := re.match("^If false: throw to monkey (\d+)$", row):
            false_target = int(regex_match.group(1))
            monkeys[monkey_id] = Monkey(
                items, operation, divisible_by, true_target, false_target
            )
    return monkeys


def _apply_relief(worry_level):
    return worry_level // 3


def _round(monkeys, _print=False):
    for monkey_id, monkey in sorted(monkeys.items()):
        if _print:
            print(f"Monkey {monkey_id}")
        for worry_level in monkey.items:
            if _print:
                print(f"Monkey inspects an item with a worry level of {worry_level}")
            worry_level = monkey.operation(worry_level)
            if _print:
                print(f"Worry level changes to {worry_level}")
            worry_level = _apply_relief(worry_level)
            if _print:
                print(
                    f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}"
                )
            if worry_level % monkey.divisible_by == 0:
                target = monkey.true_target
                if _print:
                    print(f"Current worry level is divisible by {monkey.divisible_by}")
            else:
                target = monkey.false_target
                if _print:
                    print(
                        f"Current worry level is not divisible by {monkey.divisible_by}"
                    )
            monkeys[target].items.append(worry_level)
            if _print:
                print(
                    f"Item with worry level {worry_level} is thrown to monkey {target}."
                )
        monkey.num_inspections += len(monkey.items)
        monkey.items = []
    return monkeys


def main(monkeys, _print=False):
    for i in range(20):
        monkeys = _round(monkeys, _print=_print if i == 0 else False)
        if _print:
            print(
                f"After round {i+1}, the monkeys are holding items with these worry levels:"
            )
            for monkey_id, monkey in monkeys.items():
                print(f"Monkey {monkey_id}: {','.join(map(str, monkey.items))}")
    if _print:
        for monkey_id, monkey in monkeys.items():
            print(f"Monkey {monkey_id} inspected items {monkey.num_inspections} times.")
    activity_levels = list(
        sorted(monkey.num_inspections for monkey in monkeys.values())
    )
    return activity_levels[-2] * activity_levels[-1]


if __name__ == "__main__":
    monkeys = parse_input(TEST.split("\n"))
    assert main(monkeys, _print=True) == 10605

    monkeys = parse_input(get_input(11))
    print(main(monkeys))
