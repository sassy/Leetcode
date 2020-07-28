#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = list(str(x))
        piv_index = int(len(l)/2) + 1
        max_index = len(l) - 1
        for i in range(0, piv_index - 1):
            if l[i] != l[max_index - i]:
                return False
        return True


    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(1221))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))