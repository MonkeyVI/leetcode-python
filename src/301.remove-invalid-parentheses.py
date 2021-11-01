# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by vito at 2021/10/27

__author__ = 'vito'

from typing import List

'''
301 删除无效的括号
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
返回所有可能的结果。答案可以按 任意顺序 返回。
'''


class Solution:
    res = []
    l_remove, r_remove = 0, 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        for c in s:
            if c == '(':
                self.l_remove += 1
            elif c == ')':
                if self.l_remove == 0:
                    self.r_remove += 1
                else:
                    self.l_remove -= 1
        self.helper(s, 0, self.l_remove, self.r_remove)
        return self.res

    def helper(self, s, start, l_remove, r_remove):
        if l_remove == 0 and r_remove == 0:
            if self.isValid(s):
                self.res.append(s)
            return

        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            # 如果剩余的字符无法满足去掉的数量要求，直接返回
            if l_remove + r_remove > len(s) - i:
                break
            # 尝试去掉一个左括号
            if l_remove > 0 and s[i] == '(':
                self.helper(s[:i] + s[i + 1:], i, l_remove - 1, r_remove);
            # 尝试去掉一个右括号
            if r_remove > 0 and s[i] == ')':
                self.helper(s[:i] + s[i + 1:], i, l_remove, r_remove - 1);
            # 统计当前字符串中已有的括号数量

    def isValid(self, str):
        cnt = 0
        for c in str:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0
