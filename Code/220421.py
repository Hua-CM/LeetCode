# -*- coding: utf-8 -*-
# @Time : 2022/4/21 0:22
# @Author : Zhongyi Hua
# @FileName: 220421.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if s == '':
            return ''

        stack = [s[0]]
        for c in s[1:]:
            if not stack:
                stack.append(c)
            elif stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
