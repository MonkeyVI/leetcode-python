# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/3 12:01 PM

__author__ = 'Vito'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    '''
    执行用时：56 ms, 在所有 Python3 提交中击败了59.62%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了66.87%的用户
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_l1 = []
        list_l2 = []
        res = None
        while True:
            if l1 == None:
                break;
            list_l1.append(str(l1.val))
            l1 = l1.next
        while True:
            if l2 == None:
                break;
            list_l2.append(str(l2.val))
            l2 = l2.next

        count = sum([int(''.join(list_l1)), int(''.join(list_l2))])
        for i in str(count):
            res = ListNode(int(i), res)
        return res


if __name__ == '__main__':
    l1 = [2, 4, 3]

    l2 = [5, 6, 4]
    # res = Solution().addTwoNumbers(l1, l2)
    str_a = ''
    for i in l1:
        str_a.join(l1)
    print(str_a)
