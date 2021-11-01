# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/1 10:08 AM

__author__ = 'Vito'

from typing import List

'''
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
'''


class Solution:
    """
    执行用时：80 ms, 在所有 Python3 提交中击败了82.15%的用户
    内存消耗：16.3 MB, 在所有 Python3 提交中击败了54.63%的用户
    """

    def distributeCandies(self, candyType: List[int]) -> int:
        set_candy = set(candyType)
        count = int(len(candyType) / 2)
        if len(set_candy) > count:
            res = count
        else:
            res = len(set_candy)
        return res

    def distributeCandies(self, candyType: List[int]) -> int:

        return min(len(set(candyType)), int(len(candyType) / 2))


if __name__ == '__main__':
    candies = [1, 1, 2, 2, 3, 3]
    candies = [1, 1, 2, 3]
    res = Solution().distributeCandies(candies)
    print(res)
    pass
