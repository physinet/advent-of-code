import operator
import re
from dataclasses import dataclass
from helpers import get_input

TEST = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

INV_OPERATORS = {
    "-": operator.add,
    "+": operator.sub,
    "/": operator.mul,
    "*": operator.floordiv,
}


@dataclass
class Operation:
    name1: str
    name2: str
    op: str


def parse(rows: list[str]) -> dict:
    jobs = {}
    for row in rows:
        pattern1 = "^(\D{4}): (\D{4}) (.) (\D{4})$"
        pattern2 = "^(\D{4}): (\d+)$"
        if match := re.match(pattern1, row.strip()):
            jobs[match.group(1)] = Operation(
                match.group(2), match.group(4), match.group(3)
            )
        if match := re.match(pattern2, row.strip()):
            jobs[match.group(1)] = int(match.group(2))
    return jobs


def get(jobs: dict, name: str):
    if isinstance(jobs[name], int):
        return jobs[name]
    elif isinstance(jobs[name], Operation):
        operation = jobs[name]
        return OPERATORS[operation.op](
            get(jobs, operation.name1), get(jobs, operation.name2)
        )


def inverse(jobs, val, name):
    operation = jobs[name]
    unsafe_branch = None
    for name in (operation.name1, operation.name2):
        try:
            if get(jobs, name) is not None:
                safe_branch = name
        except TypeError:
            unsafe_branch = name

    if (operation.name1 == safe_branch) and (operation.op in "-/"):
        val = OPERATORS[operation.op](get(jobs, safe_branch), val)
    else:
        val = INV_OPERATORS[operation.op](val, get(jobs, safe_branch))

    if unsafe_branch is None:
        return val

    return inverse(jobs, val, unsafe_branch)


def main2(jobs: dict) -> int:
    # Replace the human with None
    jobs["humn"] = None
    root_op = jobs["root"]

    # Find the branch that contains the human
    for name in (root_op.name1, root_op.name2):
        try:
            get(jobs, name)
            safe_branch = name
        except TypeError:
            unsafe_branch = name

    val = get(jobs, safe_branch)
    return inverse(jobs, val, unsafe_branch)


if __name__ == "__main__":
    jobs = parse(TEST.split("\n"))
    assert get(jobs, "root") == 152
    assert main2(jobs) == 301

    jobs = parse(get_input(21))
    print(get(jobs, "root"))
    print(main2(jobs))
    breakpoint()
