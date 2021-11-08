# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito at 2021/11/4 2:02 PM

__author__ = 'Vito'


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        str_a = []
        for i, c in enumerate(s):
            size = len(set(s))
            str_b = s[i:]
            str_a.append(len(set(str_b[:size])))
            print(i, size, str_b)
            # if len(set(s[i:size])) == size:
            #     str_a.append(size)
        print(str_a)
        return max(str_a)


if __name__ == '__main__':
    s = "pwwkewwww"
    # s = "aab"
    # s = "tmmzuxt"
    s = "jbpnbwwd"
    Solution().lengthOfLongestSubstring(s)
