#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))
    print(s.removeElement([], 2))