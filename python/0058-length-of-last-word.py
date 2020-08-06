#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ws = s.split()
        return len(ws[-1]) if len(ws) > 0 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord(""))