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

    def __lt__(self: "Directory", other: "Directory") -> bool:
        return self.total_size < other.total_size


N = 100_000
TOTAL_DISK_SPACE = 70_000_000
DISK_SPACE_NEEDED = 30_000_000


def parse(lines: list[str]) -> list[Directory]:
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

    all_dirs = [home]

    def _dfs(parent: Directory) -> None:
        for child in parent.children.values():
            if isinstance(child, Directory):
                _dfs(child)
                parent.total_size += child.total_size
                all_dirs.append(child)
            else:
                parent.total_size += child.size

    _dfs(home)
    return list(sorted(all_dirs))


def part1(dirs):
    return sum(d.total_size for d in dirs if d.total_size <= N)


def part2(dirs):
    unused_space = TOTAL_DISK_SPACE - dirs[-1].total_size
    space_needed = DISK_SPACE_NEEDED - unused_space
    index = bisect(dirs, space_needed, key=lambda x: x.total_size)
    return dirs[index].total_size


if __name__ == "__main__":
    dirs = parse(TEST.split("\n"))
    assert part1(dirs) == 95437
    assert part2(dirs) == 24933642

    dirs = parse(get_input(7))
    print(part1(dirs))
    print(part2(dirs))
