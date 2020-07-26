#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == '__main__': 
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
