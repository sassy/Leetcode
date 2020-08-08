#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 再帰バージョン(ネストが深すぎる/計算量が大きい)
class Solution_X:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a = self.climbStairs(n-2)
            b = self.climbStairs(n-1)
            return a + b

#　動的計画法を使う
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        if n > 2:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 45):
        print(s.climbStairs(i))
        