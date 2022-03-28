# -*- coding: utf-8 -*-
# @Time : 2022/3/12 1:55
# @Author : Zhongyi Hua
# @FileName: 220312_3.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def replaceSpace(self, s: str) -> str:
        s_array = list(s)
        s_len = len(s)
        for _ in s_array:
            if _ == ' ':
                s_array += [0,0]
        cur_l = len(s_array) - 1
        for cur_r in range(s_len-1, -1, -1):
            if s_array[cur_r] != ' ':
                s_array[cur_l] = s_array[cur_r]
                cur_l -= 1
            else:
                s_array[cur_l] = "0"
                cur_l -= 1
                s_array[cur_l] = "2"
                cur_l -= 1
                s_array[cur_l] = "%"
                cur_l -= 1
        return ''.join(s_array)
