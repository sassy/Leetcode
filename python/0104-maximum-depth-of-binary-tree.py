#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def builder(nums:List) -> TreeNode:
    nodes = [TreeNode(num) for num in nums]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if kids:
            node.left = kids.pop()
            node.right = kids.pop()
    return root

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            depth = max(self.maxDepth(root.right), self.maxDepth(root.left))
            return depth + 1


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth(builder([3,9,20,None,None,15,7])))