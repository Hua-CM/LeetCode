# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 18:19
# @Author  : Zhongyi Hua
# @File    : 220220_3.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head
        pre = None
        for _step in range(n-1):
            fast = fast.next
        while fast.next is not None:
            pre = slow
            fast = fast.next
            slow = slow.next
        pre.next = slow.next
        return dummy_head.next
