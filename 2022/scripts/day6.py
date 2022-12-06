from helpers import get_input
from collections import Counter

TEST_CASES = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
)


def main(text):
    counter = Counter(text[:4])
    i = 4
    while sum(x != 0 for x in counter.values()) != 4:
        counter[text[i]] += 1
        counter[text[i - 4]] -= 1
        i += 1
    return i


if __name__ == "__main__":
    for case, result in TEST_CASES:
        assert main(case) == result
    (text,) = get_input(6)
    print(main(text))
