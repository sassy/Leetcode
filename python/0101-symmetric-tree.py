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
    def compareTree(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val == right.val:
            return self.compareTree(left.left, right.right) and self.compareTree(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.compareTree(root.left, root.right)
        

if __name__ == '__main__':
    s = Solution()
    root = builder([1,2,2,3,4,4,3])
    print(s.isSymmetric(root))  # True
    root = builder([1,2,2,None,3,None,3])
    print(s.isSymmetric(root))  # False
    root = builder([2,3,3,4,5,None,4])
    print(s.isSymmetric(root))  # False

    
