#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        nums = list(str(x))
        head = nums.pop(0) if nums[0] == '-' else ''
        nums.reverse()
        ret = int(head + ''.join(nums))
        return 0 if ret >= 2147483647 or ret <= -2147483648 else ret

if __name__ == '__main__': 
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(1534236469))
