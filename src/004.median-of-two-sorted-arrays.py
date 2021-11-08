# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/4 10:50 AM

__author__ = 'Vito'

from typing import List

'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
'''
class Solution:
    '''
    执行用时：44 ms, 在所有 Python3 提交中击败了61.24%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了58.58%的用户
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        count = int(len(nums1) // 2)
        if len(nums1) % 2 == 0:
            res_list = nums1[count - 1:count + 1]
        else:
            return nums1[count]

        return sum(res_list) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
