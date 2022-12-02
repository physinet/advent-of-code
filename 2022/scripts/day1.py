from helpers import get_input
from heapq import heappush, nlargest


def calories(n) -> int:
    calories_per_elf = []
    running_total = 0
    for row in get_input(1):
        match row:
            case cals if cals.strip():
                running_total += int(cals)
            case _:
                heappush(calories_per_elf, running_total)
                running_total = 0

    return sum(nlargest(n, calories_per_elf))


if __name__ == "__main__":
    print(calories(1))
    print(calories(3))
