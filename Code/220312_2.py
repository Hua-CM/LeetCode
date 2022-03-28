# -*- coding: utf-8 -*-
# @Time : 2022/3/12 1:48
# @Author : Zhongyi Hua
# @FileName: 220312_2.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        cur_l = 0
        cur_r = len(s) -1
        while cur_l <= cur_r:
            s[cur_r], s[cur_l] = s[cur_l], s[cur_r]
            cur_l += 1
            cur_r -= 1
