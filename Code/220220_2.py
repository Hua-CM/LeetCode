# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 16:41
# @Author  : Zhongyi Hua
# @File    : 220220_2.py.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head is None) or (head.next is None):
            return head
        else:
            dummy_head = ListNode(0, head.next)
            current = head
            while (current is not None) and (current.next is not None):
                next_ = current.next
                tmp = next_.next
                tmp2 = tmp.next if tmp is not None else None
                next_.next = current
                current.next = tmp2 if tmp2 is not None else tmp
                current = tmp
            return dummy_head.next


