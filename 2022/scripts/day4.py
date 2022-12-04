from helpers import get_input
from typing import Iterable

TEST = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]

SectionRange = tuple[int, int]


def pair_sections(row: str) -> tuple[SectionRange, SectionRange]:
    return tuple(tuple(int(sec) for sec in elf.split("-")) for elf in row.split(","))


def fully_contains(sec1: SectionRange, sec2: SectionRange) -> bool:
    return (sec1[0] <= sec2[0] and sec1[1] >= sec2[1]) or (
        sec2[0] <= sec1[0] and sec2[1] >= sec1[1]
    )


if __name__ == "__main__":
    assert sum(fully_contains(*pair_sections(row)) for row in TEST) == 2
    print(sum(fully_contains(*pair_sections(row)) for row in get_input(4)))
