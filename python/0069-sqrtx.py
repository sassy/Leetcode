#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))