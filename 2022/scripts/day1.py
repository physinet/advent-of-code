from helpers import get_input
from heapq import heappush, nlargest


def calories(n) -> int:
    calories_per_elf = []
    running_total = 0
    for row in get_input(1):
        if cals := row.strip():
            running_total += int(cals)
        else:
            heappush(calories_per_elf, running_total)
            running_total = 0

    return sum(nlargest(n, calories_per_elf))


if __name__ == "__main__":
    print(calories(1))
    print(calories(3))
