#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution_x:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i,v in enumerate(nums1):
            if j >= n:
                break
            if v >= nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
        for i in range(j,n):
            nums1.insert(i + m, nums2[i])
        del nums1[m+n:]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()


if __name__ == '__main__':
    s = Solution2()
    nums1 = [1,2,3,0,0,0]
    s.merge(nums1, 3, [2,5,6], 3)
    print(nums1)
    nums1 = [-1,0,0,3,3,3,0,0,0]
    s.merge(nums1, 6, [1,2,2], 3)
    print(nums1)  # [-1,0,0,1,2,2,3,3,3]
    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    print(nums1)  
