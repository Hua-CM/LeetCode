# -*- coding: utf-8 -*-
# @Time : 2022/4/14 0:15
# @Author : Zhongyi Hua
# @FileName: 220414.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        while len(self.queue) > 1:
            self.queue2.append(self.queue.popleft())
        self.queue, self.queue2 = self.queue2, self.queue
        return self.queue2.popleft()

    def top(self) -> int:
        if self.empty():
            return None

        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()