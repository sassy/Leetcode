#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"
        else:
            seq = self.countAndSay(n-1)
            count = 1
            ret = ""
            for i, v in enumerate(seq):
                if i < len(seq) - 1 and seq[i] == seq[i+1]:
                    count += 1
                else:
                    ret += str(count) + str(v)
                    count = 1
            return ret
                

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))
    print(s.countAndSay(6))
    print(s.countAndSay(7))
    print(s.countAndSay(8))
    print(s.countAndSay(9))
    print(s.countAndSay(10))