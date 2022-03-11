# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 15:47
# @Author  : Zhongyi Hua
# @File    : 220301_3.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        str_list = list(s)
        s_len = len(str_list)
        for _start in range(0, s_len, 2*k):
            left = _start
            right = min(_start + k - 1, s_len - 1)
            while left <= right:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1
        return ''.join(str_list)