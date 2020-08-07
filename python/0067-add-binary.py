#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int (b, 2), 'b')

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11",  "1"))
    print(s.addBinary("1010",  "1011"))