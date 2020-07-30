#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        while len(s) != 0:
            if s[0:2] == 'CM':
                count += 900
                s = s[2:]
            elif s[0] == 'M':
                count += 1000
                s = s[1:]
            elif s[0:2] == 'CD':
                count += 400
                s = s[2:]
            elif s[0] == 'D':
                count += 500
                s = s[1:]
            elif s[0:2] == 'XC':
                count += 90
                s = s[2:]
            elif s[0] == 'C':
                count += 100
                s = s[1:]
            elif s[0:2] == 'XL':
                count += 40
                s = s[2:]
            elif s[0] == 'L':
                count += 50
                s = s[1:]
            elif s[0:2] == 'IX':
                count += 9
                s = s[2:]
            elif s[0] == 'X':
                count += 10
                s = s[1:]
            elif s[0:2] == 'IV':
                count += 4
                s = s[2:]
            elif s[0] == 'V':
                count += 5
                s = s[1:]
            elif s[0] == 'I':
                count += 1
                s = s[1:]
            else:
                return  0
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('I')) #1
    print(s.romanToInt('III')) #3
    print(s.romanToInt('IV')) #4
    print(s.romanToInt('IX')) #9
    print(s.romanToInt('LVIII')) #58
    print(s.romanToInt('MCMXCIV')) #1994
