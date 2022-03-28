# -*- coding: utf-8 -*-
# @Time : 2022/3/29 0:37
# @Author : Zhongyi Hua
# @FileName: 220329.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        if len(self.stack_in) == len(self.stack_out) == 0:
            return True
        else:
            return False
