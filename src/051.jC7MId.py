# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/1 10:25 AM

__author__ = 'Vito'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def dfs_NLR(x: TreeNode) -> int:
            nonlocal res
            if x == None:
                return 0

            l = dfs_NLR(x.left)
            r = dfs_NLR(x.right)

            cur_sum = x.val + max(0, l) + max(0, r)
            res = max(res, cur_sum)

            return x.val + max(max(0, l), max(0, r))

        dfs_NLR(root)
        return res


if __name__ == '__main__':
    root = [-10, 9, 20, None, None, 15, 7]
    # root = [1, 2, 3]
    res = Solution().maxPathSum(root)
    print(res)
