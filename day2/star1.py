# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>


class WTFException(Exception):
    pass


def main():
    parsed = []
    with open("input.txt") as f:
        for line in f:
            s = line.split()
            parsed.append((s[0], int(s[1])))

    stats = [0, 0]

    for cmd in parsed:
        if cmd[0] == "forward":
            stats[0] += cmd[1]
        elif cmd[0] == "up":
            stats[1] -= cmd[1]
        elif cmd[0] == "down":
            stats[1] += cmd[1]
        else:
            raise WTFException

    print(stats)
    print(stats[0] * stats[1])


if __name__ == "__main__":
    main()
