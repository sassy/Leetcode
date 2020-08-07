#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i, v in enumerate(digits):
            sum = sum * 10 + v
        sum = sum + 1
        return list(map(int, list(str(sum))))
        

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4,3,2,1]))