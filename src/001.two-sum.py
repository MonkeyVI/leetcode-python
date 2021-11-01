# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/10/29 2:47 PM

__author__ = 'Vito'

from typing import List

'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

'''


class Solution:
    """
    执行用时：3032 ms, 在所有 Python3 提交中击败了24.17%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了76.10%的用户
    通过测试用例：55 / 55
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        n_index = 0
        for i in nums:
            m_index = 0
            for nj in nums[n_index + 1:]:
                if (i + nj) == target:
                    res.append(n_index)
                    res.append(m_index + n_index + 1)
                m_index += 1
            n_index += 1

        return res

    """
    执行用时：3900 ms, 在所有 Python3 提交中击败了6.72%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了55.00%的用户
    通过测试用例：55 / 55
    """

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in enumerate(nums):
            nums_1 = nums[i[0] + 1:]
            for nj in enumerate(nums_1):
                if (i[1] + nj[1]) == target:
                    res.append(i[0])
                    res.append(i[0] + nj[0] + 1)

        return res

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            result = target-num
            if result in hashtable:
                return [hashtable[result], i]
            hashtable[nums[i]] = i
        return []



if __name__ == '__main__':
    nums = [3, 2, 4]
    # nums = [3, 3]
    target = 6
    twosum = Solution().twoSum1(nums=nums, target=target)
    print(twosum)
