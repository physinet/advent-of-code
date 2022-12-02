from collections import defaultdict
from helpers import get_input


def main() -> int:
    bin_strings = [row.strip() for row in get_input(3)]
    N = len(bin_strings)
    bits = len(bin_strings[0])

    sums = [sum(int(string[i]) for string in bin_strings) for i in range(bits)]
    gamma = int("".join(str(int(sum >= N / 2)) for sum in sums), 2)
    epsilon = gamma ^ (2**bits - 1)
    return gamma * epsilon


def main2() -> int:
    bin_strings = [row.strip() for row in get_input(3)]

    def rating(bin_strings, function):
        n = 0
        while len(bin_strings) > 1:
            d = defaultdict(list)
            for string in bin_strings:
                d[string[n]].append(string)
            n += 1
            bin_strings = function(d)
        return int(bin_strings[0], 2)

    oxygen_function = lambda d: max(d["1"], d["0"], key=lambda x: len(x))
    oxygen = rating(bin_strings, oxygen_function)

    co2_function = lambda d: min(d["0"], d["1"], key=lambda x: len(x))
    co2 = rating(bin_strings, co2_function)

    return oxygen * co2


if __name__ == "__main__":
    print(main())
    print(main2())
