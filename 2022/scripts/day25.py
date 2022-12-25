from helpers import get_input

EXAMPLES = (
    (1, "1"),
    (2, "2"),
    (3, "1="),
    (4, "1-"),
    (5, "10"),
    (6, "11"),
    (7, "12"),
    (8, "2="),
    (9, "2-"),
    (10, "20"),
    (15, "1=0"),
    (20, "1-0"),
    (2022, "1=11-2"),
    (12345, "1-0---0"),
    (314159265, "1121-1110-1=0"),
)

TEST = (
    ("1=-0-2", 1747),
    ("12111", 906),
    ("2=0=", 198),
    ("21", 11),
    ("2=01", 201),
    ("111", 31),
    ("20012", 1257),
    ("112", 32),
    ("1=-1=", 353),
    ("1-12", 107),
    ("12", 7),
    ("1=", 3),
    ("122", 37),
)

CHAR_TO_NUM = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
NUM_TO_CHAR = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}


def from_snafu(s: str) -> int:
    return sum(CHAR_TO_NUM[c] * 5**i for i, c in enumerate(reversed(s)))


def to_snafu(num: int) -> str:
    s = ""
    while True:
        num += 2
        floor = num // 5
        s += to_snafu(floor)
        num = num % 5 - 2
        if num <= 2:
            break
    s += NUM_TO_CHAR[num]
    return s.lstrip("0")


def to_snafu(num: int) -> str:
    s = ""
    while True:
        if num in (-2, -1, 0, 1, 2):
            s += NUM_TO_CHAR[num]
            break
        else:
            floor = (num + 2) // 5
            s += to_snafu(floor)
            num = (num + 2) % 5 - 2
    return s


if __name__ == "__main__":
    for num, snafu in EXAMPLES:
        assert to_snafu(num) == snafu
        assert from_snafu(snafu) == num
    tot = 0
    for snafu, check_num in TEST:
        assert to_snafu(check_num) == snafu
        assert (num := from_snafu(snafu)) == check_num
        tot += num
    assert tot == 4890
    assert to_snafu(tot) == "2=-1=0"

    tot = 0
    for snafu in get_input(25):
        tot += from_snafu(snafu.strip())

    print(to_snafu(tot))
