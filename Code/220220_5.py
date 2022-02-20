# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 19:59
# @Author  : Zhongyi Hua
# @File    : 220220_5.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        already_set = dict()
        index = 0
        cur = head
        while True:
            already_set[cur] = index
            if cur.next is None or cur.next in already_set:
                break
            cur = cur.next
            index += 1
        return cur.next
