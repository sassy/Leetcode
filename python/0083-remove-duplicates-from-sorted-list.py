#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    @classmethod
    def builder(cls, l):
        l.reverse()
        if len(l) < 1:
            return
        prev = None
        for e in l:
            node = ListNode(val=e, next=prev)
            prev = node
        return node

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        print(self.val, end="")
        if self.next:
            print('->', end="")
            self.next.print()
        else:
            print()

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        cache = head.val
        prev = head
        node = head.next
        while True:
            if node == None:
                return head
            if cache == node.val:
                prev.next = node.next
            else:
                prev = node
            cache = node.val
            node = node.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode.builder([1,1,2])
    s.deleteDuplicates(head).print()
    head = ListNode.builder([1,1,2,3,3])
    s.deleteDuplicates(head).print()
    head = ListNode.builder([1,2,3,4,5,5,5])
    s.deleteDuplicates(head).print()
    head = ListNode.builder([])
    print(s.deleteDuplicates(head))