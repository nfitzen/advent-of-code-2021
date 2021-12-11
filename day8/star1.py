#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

import itertools
import math


def main():
    with open("input.txt") as f:
        data = []
        for line in f:
            data.extend(line.split(" | ")[1].strip().split(" "))

        mapping = {1: 2, 4: 4, 7: 3, 8: 7}

        mapping = {v: k for k, v in mapping.items()}

        print(len(tuple(i for i in data if len(i) in mapping)))


if __name__ == "__main__":
    main()
