# -*- coding: utf-8 -*-
# @Time : 2022/4/21 0:43
# @Author : Zhongyi Hua
# @FileName: 220421_2.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        formula_dict = {'+': lambda x, y: x+y,
                        '-': lambda x, y: x-y,
                        '*': lambda x, y: x*y,
                        '/': lambda x, y: int(x/y)}
        for c in tokens:
            formula = formula_dict.get(c)
            if formula:
                right = stack.pop()
                left = stack.pop()
                stack.append(formula(left, right))
            else:
                stack.append(int(c))
        return int(stack[0])
