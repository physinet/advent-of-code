from collections import Counter, defaultdict

from helpers import get_input


def main(data: list[int], /, *, days: int = 80) -> int:
    fishes = Counter(data)
    for _ in range(days):
        fishes = defaultdict(int, {timer - 1: count for timer, count in fishes.items()})
        new_fishes = fishes.pop(-1, 0)
        fishes[6] += new_fishes
        fishes[8] += new_fishes

    return sum(fishes.values())


if __name__ == "__main__":
    test_data = [3, 4, 3, 1, 2]
    print(main(test_data, days=18))
    print(main(test_data, days=80))

    data = list(map(int, get_input(6)[0].split(",")))
    print(main(data, days=80))
    print(main(data, days=256))
