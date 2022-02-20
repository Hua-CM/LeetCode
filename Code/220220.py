# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 16:23
# @Author  : Zhongyi Hua
# @File    : 220220.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
