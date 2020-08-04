#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([], 0))

