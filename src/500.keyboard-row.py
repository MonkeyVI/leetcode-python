# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/1 8:43 AM

__author__ = 'Vito'

from typing import List

'''
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：
第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

'''

class Solution:
    '''
    执行用时：32 ms, 在所有 Python3 提交中击败了63.31%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了26.04%的用户
    '''

    def findWords(self, words: List[str]) -> List[str]:
        res = []
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        for word in words:
            a = [i for i in word if i in first_row]
            b = [i for i in word if i in second_row]
            c = [i for i in word if i in third_row]
            if len(a) == len(word):
                res.append(word)
            if len(b) == len(word):
                res.append(word)
            if len(c) == len(word):
                res.append(word)
        return res
