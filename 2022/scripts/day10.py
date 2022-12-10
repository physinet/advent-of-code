from helpers import get_input

TEST = """noop
addx 3
addx -5"""

TEST2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def get_cycle_values(rows):
    x_vals = [1]
    for row in rows:
        x_vals.append(x_vals[-1])
        if row.strip() == "noop":
            continue
        else:
            x_vals.append(x_vals[-1] + int(row.strip().split()[-1]))
    return x_vals


def get_interesting_signal_strengths(values):
    return [values[i - 1] * i for i in range(20, len(values), 40)]


def draw(cycle_values):
    s = ""
    for i, value in enumerate(cycle_values):
        if i % 40 == 0:
            s += "\n"
        if value - 1 <= i % 40 <= value + 1:
            s += "#"
        else:
            s += "."
    return s


if __name__ == "__main__":
    assert get_cycle_values(TEST.split("\n")) == [1, 1, 1, 4, 4, -1]

    cycle_values = get_cycle_values(TEST2.split("\n"))
    assert (strengths := get_interesting_signal_strengths(cycle_values)) == [
        420,
        1140,
        1800,
        2940,
        2880,
        3960,
    ]
    assert sum(strengths) == 13140
    print(draw(cycle_values))

    cycle_values = get_cycle_values(get_input(10))
    strengths = get_interesting_signal_strengths(cycle_values)
    print(sum(strengths))
    print(draw(cycle_values))
