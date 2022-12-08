import heapq
from bisect import bisect
from typing import Union
from dataclasses import dataclass, field
from helpers import get_input

TEST = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: "Directory" = None
    children: dict[str, Union["Directory", File]] = field(default_factory=dict)
    total_size: int = 0

    def __lt__(self, other):
        return self.total_size < other.total_size


N = 100_000
TOTAL_DISK_SPACE = 70_000_000


def parse(lines):
    home = directory = Directory("/")
    for line in lines[1:]:  # skip initial $ cd /
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            match line.split()[-1]:
                case "..":
                    directory = directory.parent
                case name:
                    directory = directory.children.setdefault(
                        name, Directory(name, directory)
                    )
        elif line.startswith("dir"):
            _, name = line.split()
            directory.children.setdefault(name, Directory(name, directory))
        else:
            size, name = line.split()
            directory.children.setdefault(name, File(name, int(size)))

    heap = [home]

    def _dfs(parent):
        for child in parent.children.values():
            if isinstance(child, Directory):
                _dfs(child)
                parent.total_size += child.total_size
                heapq.heappush(heap, child)
            else:
                parent.total_size += child.size

    _dfs(home)
    return heap


def part1(dirs):
    return sum(d.total_size for d in dirs if d.total_size <= N)


if __name__ == "__main__":
    dirs = parse(TEST.split("\n"))
    assert part1(dirs) == 95437

    dirs = parse(get_input(7))
    print(part1(dirs))
