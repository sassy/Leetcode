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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        array: List[List[int]] = []
        level = []
        left: List[List[int]] = []
        right: List[List[int]] = []
        if root.left != None:
            left = self.levelOrderBottom(root.left)
        if root.right != None:
            right = self.levelOrderBottom(root.right)
        
        print("left ", left)
        print("right ", right)
        for l, r in zip(left, right):
            if type(l) is list and type(r) is list:
                l2 = [x for x in l if x]
                r2 = [x for x in r if x]
                if len(l2) > 0 and len(r2) > 0:
                    l2.extend(r2)
                    array.append(l2)
                elif len(l2) > 0:
                    array.append(l2)
                elif len(r2) > 0:
                    array.append(r2)
        if root != None:
            array.append([root.val])
        return array

if __name__ == '__main__':
    s = Solution()
    print(s.levelOrderBottom(builder([3,9,20,None,None,15,7])))
