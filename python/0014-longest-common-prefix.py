#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_len = len(strs)
        min_len = len(strs[0]) if strs_len > 0 else 0
        for str in strs:
            strlen = len(str)
            min_len = strlen if strlen < min_len else min_len
        ret = ''
        for i in range(min_len):
            common = True
            for j in range(strs_len - 1):
                if strs[j][i] != strs[j+1][i]:
                    common = False
            if common:
                ret += strs[0][i]
            else:
                return ret
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"])) # "fl"
    print(s.longestCommonPrefix(["dog","racecar","car"])) # ""
    print(s.longestCommonPrefix([])) # ""