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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1        
        if l1.val <= l2.val:
            head1 = l1.next
            head2 = l2
            new_list = new_list_head = l1
        else:
            head1 = l1
            head2 = l2.next
            new_list = new_list_head = l2
        while head1 != None or head2 != None:
            if head1 == None:
                new_list_head.next = head2
                return new_list
            elif head2 == None:
                new_list_head.next = head1
                return new_list
            if head1.val <= head2.val:
                new_list_head.next = head1
                new_list_head = new_list_head.next
                head1 = head1.next
            else:
                new_list_head.next = head2
                new_list_head = new_list_head.next
                head2 = head2.next
        return new_list


if __name__ == '__main__':
    s = Solution()
    s.mergeTwoLists(ListNode.builder([1, 2, 4]), ListNode.builder([1, 3, 4])).print()
    s.mergeTwoLists(ListNode.builder([1, 2, 3, 4]), ListNode.builder([1, 3, 4])).print()
    s.mergeTwoLists(ListNode.builder([]), ListNode.builder([1, 3, 4])).print()
    s.mergeTwoLists(ListNode.builder([1, 2, 4]), ListNode.builder([])).print()
    print(s.mergeTwoLists(ListNode.builder([]), ListNode.builder([])))
    s.mergeTwoLists(ListNode.builder([1]), ListNode.builder([1])).print()
    s.mergeTwoLists(ListNode.builder([1]), ListNode.builder([2])).print()
    s.mergeTwoLists(ListNode.builder([2]), ListNode.builder([1])).print()
    

