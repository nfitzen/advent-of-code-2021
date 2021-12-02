# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>


def main():
    prev = 0
    increased = -1
    with open("input.txt") as f:
        for number in map(int, f):
            if number > prev:
                increased += 1
            prev = number
    print(increased)


if __name__ == "__main__":
    main()
