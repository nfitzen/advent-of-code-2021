# SPDX-License-Identifier: MIT
# Copyright (C) 2021 nfitzen <https://github.com/nfitzen>

import itertools
import math


def main():
    with open("input.txt") as f:
        data = f.readlines()
    data = [l.strip() for l in data]

    tmpList = data.copy()
    position = 0
    while len(tmpList) > 1:
        freq = [0, 0]
        if len(tmpList) == 1:
            break
        for line in tmpList:
            if int(line[position], 2):
                freq[0] += 1
            else:
                freq[1] += 1
        mostfreq = "1" if freq[0] >= freq[1] else "0"
        tmpList2 = []
        for line in tmpList:
            if line[position] == mostfreq:
                tmpList2.append(line)
        tmpList = tmpList2
        position += 1

    o2r = int(tmpList[0], 2)

    print(o2r)

    tmpList = data.copy()
    position = 0
    while len(tmpList) > 1:
        freq = [0, 0]
        if len(tmpList) == 1:
            break
        for line in tmpList:
            if int(line[position], 2):
                freq[0] += 1
            else:
                freq[1] += 1
        leastfreq = "1" if freq[0] < freq[1] else "0"
        tmpList2 = []
        for line in tmpList:
            if line[position] == leastfreq:
                tmpList2.append(line)
        tmpList = tmpList2
        position += 1

    co2r = int(tmpList[0], 2)

    print(co2r)

    print(o2r * co2r)


if __name__ == "__main__":
    main()
