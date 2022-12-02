from helpers import get_input


def main() -> int:
    horizontal = 0
    depth = 0
    for command, value in map(lambda x: x.split(" "), get_input(2)):
        value = int(value)
        match command:
            case "forward":
                horizontal += value
            case "down":
                depth += value
            case "up":
                depth -= value
    return horizontal * depth

def main2() -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for command, value in map(lambda x: x.split(" "), get_input(2)):
        value = int(value)
        match command:
            case "forward":
                horizontal += value
                depth += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value
    return horizontal * depth


if __name__ == "__main__":
    print(main())
    print(main2())


