# -*- coding: utf-8 -*-
# @Time : 2022/2/19 15:49
# @Author : Zhongyi Hua
# @FileName: 220219.py
# @Usage: LeetCode 707
# @Note:
# @E-mail: njbxhzy@hotmail.com

class ListNode:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class MyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
            if node is None:
                break
        val = -1 if node is None else node.val
        return val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, next_=self.head)
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        node = self.head
        if not self.head:
            self.head = new_tail
        else:
            while node.next is not None:
                node = node.next
            node.next = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index > 0:
            node = self.head
            while index > 0:
                if (node is None) and (index != 0):
                    return
                index -= 1
                parent = node
                node = node.next
            add_node = ListNode(val, node)
            parent.next = add_node
        else:
            if self.head is None:
                self.head = ListNode(val, None)
            else:
                add_node = ListNode(val, self.head)
                self.head = add_node

    def deleteAtIndex(self, index: int) -> None:
        dummy_head = ListNode(0, next_=self.head)
        index += 1
        if index > 0:
            node = dummy_head
            while index > 0:
                parent = node
                node = node.next
                index -= 1
                if node is None:
                    return
            parent.next = node.next
            if parent is dummy_head:
                self.head = parent.next
