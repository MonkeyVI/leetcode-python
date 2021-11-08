# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/4 10:17 AM

__author__ = 'Vito'

import math

'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
'''


class Solution:
    '''
    执行用时：28 ms, 在所有 Python3 提交中击败了87.69%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了75.32%的用户
    '''

    def isPerfectSquare(self, num: int) -> bool:
        return math.sqrt(num).is_integer()

    def isPerfectSquare1(self, num: int) -> bool:
        num1 = 1
        while num > 0:
            num -= num1;
            num1 += 2;
        return num == 0;


if __name__ == '__main__':
    Solution().isPerfectSquare(16)
