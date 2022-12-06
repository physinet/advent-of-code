import re
from helpers import get_input

TEST = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def setup_stacks(rows):
    stack_of_rows = []
    for row_num, row in enumerate(rows):
        if row[1].isdigit():
            break
        stack_of_rows.append(row)
    num_stacks = int(row.strip().split()[-1])
    stacks = [[] for _ in range(num_stacks)]
    while stack_of_rows:
        row = stack_of_rows.pop()
        for i in range(num_stacks):
            if (char := row[4 * i + 1]).isalpha():
                stacks[i].append(char)
    return stacks, row_num


def parse_move(move):
    regex = re.search("move (\d+) from (\d+) to (\d+)", move)
    return tuple(int(regex.group(i + 1)) for i in range(3))


def make_moves(stacks, rows):
    for row in rows:
        num, src, dst = parse_move(row)
        for _ in range(num):
            stacks[dst - 1].append(stacks[src - 1].pop())
    return stacks


def make_moves_ordered(stacks, rows):
    for row in rows:
        num, src, dst = parse_move(row)
        stacks[dst - 1].extend(stacks[src - 1][-num:])
        stacks[src - 1] = stacks[src - 1][:-num]
    return stacks


def get_result(stacks):
    return "".join(stack[-1] if len(stack) > 0 else " " for stack in stacks)


def main(rows, fn):
    stacks, row_num = setup_stacks(rows)
    stacks = fn(stacks, rows[row_num + 2 :])
    return get_result(stacks)


if __name__ == "__main__":
    print(main(TEST.split("\n"), make_moves))
    print(main(get_input(5), make_moves))
    print(main(TEST.split("\n"), make_moves_ordered))
    print(main(get_input(5), make_moves_ordered))
