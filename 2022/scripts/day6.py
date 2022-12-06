from helpers import get_input
from collections import Counter

TEST_CASES = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
)


def main(text, N):
    counter = Counter(text[:N])
    i = N
    while sum(x != 0 for x in counter.values()) != N:
        counter[text[i]] += 1
        counter[text[i - N]] -= 1
        i += 1
    return i


if __name__ == "__main__":
    for case, result4, result14 in TEST_CASES:
        assert main(case, 4) == result4
        assert main(case, 14) == result14
    (text,) = get_input(6)
    print(main(text, 4))
    print(main(text, 14))
