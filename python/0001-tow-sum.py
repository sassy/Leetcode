#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            else:
                hashtable[num] = i

if __name__ == '__main__': 
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
