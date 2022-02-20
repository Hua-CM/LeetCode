# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 18:50
# @Author  : Zhongyi Hua
# @File    : 220220_4.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dummy_headA = ListNode(next=headA)
        dummy_headB = ListNode(next=headB)
        curA = dummy_headA
        curB = dummy_headB
        lenA = 0
        lenB = 0
        while curA.next:
            lenA += 1
            curA = curA.next
        while curB.next:
            lenB += 1
            curB = curB.next
        if lenA > lenB:
        # keep sure B is always the longer one
            lenB, lenA = lenA, lenB
            curB = dummy_headA
            curA = dummy_headB
        else:
            curA = dummy_headA
            curB = dummy_headB

        for _ in range(lenB - lenA):
            curB = curB.next

        while curA:
            if curB is curA:
                return curA
            curB = curB.next
            curA = curA.next

        return None