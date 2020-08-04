#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        return match.span()[0] if match is not None else -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr( "hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
    print(s.strStr("aaaaa", ""))
    print(s.strStr("", "a"))
    print(s.strStr("", ""))
    print(s.strStr("aaaaa", "aaa"))