from helpers import get_input


def f(x: int, quad: bool = False) -> int:
    return int(0.5 * x * (x + 1) if quad else x)


def main(data: list[int], cost_increase: bool = False) -> int:
    min_fuel = 1e99
    for pos in range(min(data), max(data)):
        min_fuel = min(min_fuel, sum((f(abs(pos - x), cost_increase) for x in data)))

    return min_fuel


if __name__ == "__main__":
    test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    print(main(test_data))

    data = list(map(int, get_input(7)[0].split(",")))
    print(main(data))

    test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    print(main(test_data, cost_increase=1))

    data = list(map(int, get_input(7)[0].split(",")))
    print(main(data, cost_increase=1))
