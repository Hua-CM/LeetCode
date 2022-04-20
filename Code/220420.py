# -*- coding: utf-8 -*-
# @Time : 2022/4/14 0:39
# @Author : Zhongyi Hua
# @FileName: 220420.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        map_dict = {'{': '}',
                    '[': ']',
                    '(': ')'}
        stack = []
        for c in s:
            if c in map_dict:
                stack.append(map_dict.get(c))
            elif len(stack) == 0:
                return False
            else:
                right_ = stack.pop()
                if not right_ == c:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

