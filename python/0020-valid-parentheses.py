#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)
        stack = []
        while len(l) != 0:
            head = l.pop(0)
            if head == '(' or head == '{' or head == '[':
                stack.append(head)
            elif head == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif len(stack) > 0 and head == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            elif len(stack) > 0 and head == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()")) #True
    print(s.isValid("()[]{}")) #True
    print(s.isValid( "(]")) #False
    print(s.isValid("([)]")) #False
    print(s.isValid("{[]}")) #True
    print(s.isValid("[")) #False
    print(s.isValid("]")) #False
    print(s.isValid("")) #False
        