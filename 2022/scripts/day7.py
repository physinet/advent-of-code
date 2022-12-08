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


N = 100000


def main(lines):
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

    def _dfs(directory, total):
        for directory_or_file in directory.children.values():
            if isinstance(directory_or_file, Directory):
                _, total = _dfs(directory_or_file, total)
                directory.total_size += directory_or_file.total_size
                if directory_or_file.total_size <= N:
                    total += directory_or_file.total_size
            else:
                directory.total_size += directory_or_file.size
        return directory, total

    _, total = _dfs(home, 0)
    return total


if __name__ == "__main__":
    assert main(TEST.split("\n")) == 95437
    print(main(get_input(7)))
