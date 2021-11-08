# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/5 10:34 AM

__author__ = 'Vito'

from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        for v in arr:
            print(v, dp[v], dp[v - difference])
            dp[v] = dp[v - difference] + 1
            print(dp[v])
            print('--------')
        return max(dp.values())


if __name__ == '__main__':
    # arr = [1, 3, 5, 7]
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    # difference = 1
    difference = -2
    print(Solution().longestSubsequence(arr, difference))
