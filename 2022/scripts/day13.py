from helpers import get_input
from itertools import zip_longest

TEST = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

Pair = tuple[list, list]


def packet_pairs(rows: list[str]) -> list[Pair]:
    packet1, packet2 = None, None
    pairs = []
    for row in rows:
        if not row.strip():
            continue
        if packet1 is None:
            packet1 = eval(row)  # 😬
        elif packet2 is None:
            packet2 = eval(row)  # 😬
            pairs.append((packet1, packet2))
            packet1, packet2 = None, None
    return pairs


def ordered(left: int | list | None, right: int | list | None) -> bool:
    if not isinstance(left, list) and not isinstance(right, list):
        return left < right
    left_val = left if isinstance(left, list) else [left]
    right_val = right if isinstance(right, list) else [right]
    for l, r in zip_longest(left_val, right_val):
        if l is None:
            return True
        if r is None:
            return False
        if l == r:
            continue
        _ordered = ordered(l, r)
        if _ordered is not None:
            return _ordered


def main(rows):
    pairs = packet_pairs(rows)
    indices = (i + 1 for i, pair in enumerate(pairs) if ordered(*pair))
    return sum(indices)


if __name__ == "__main__":
    assert ordered([[[10]], 1], [[10], 2])  # debug case
    assert main(TEST.split("\n")) == 13
    print(main(get_input(13)))
