# -*- coding: utf-8 -*-
# @Time : 2022/4/25 0:29
# @Author : Zhongyi Hua
# @FileName: 220425.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

from collections import deque


class MyDeque:
    def __init__(self, initq: deque):
        self.window = initq
        self.queue = self._initq_(initq)

    def _initq_(self, queue):
        _return_q = [queue[0]]
        for _k in range(1, len(queue)):
            while queue[_k] > _return_q[-1]:
                _return_q.pop()
                if not _return_q:
                    break
            _return_q.append(queue[_k])
        return deque(_return_q)

    def front(self, value):
        # push
        self.window.append(value)
        # pop
        popvalue = self.window.popleft()
        if popvalue == self.queue[0]:
            self.queue.popleft()
        if self.queue:
            while self.queue[-1] < value:
                self.queue.pop()
                if not self.queue:
                    break
            self.queue.append(value)
        else:
            self.queue.append(value)

        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        queue = MyDeque(initq=deque(nums[0:k]))
        res_lst = [queue.queue[0]]
        for idx in range(k, len(nums)):
            res_lst.append(queue.front(nums[idx]))
        return res_lst
