# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/1 11:37 AM

__author__ = 'Vito'

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []
        ord_a = ord('a')
        X = sum(shifts) % 26
        for i, c in enumerate(s):
            index = ord(c) - ord_a
            res.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26
        return "".join(res)


if __name__ == '__main__':
    s = 'ruu'
    shifts = [26, 9, 17]
    res = Solution().shiftingLetters(s, shifts)
    print(res)
