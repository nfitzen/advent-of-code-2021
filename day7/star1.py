#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

from statistics import median


def main():
    with open("input.txt") as f:
        data = [int(i) for i in f.readline().split(",")]

    med = round(median(data))

    print(sum(abs(i - med) for i in data))


if __name__ == "__main__":
    main()
