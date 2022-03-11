# -*- coding: utf-8 -*-
# @Time : 2022/3/10 0:48
# @Author : Zhongyi Hua
# @FileName: 220310.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len = len(s)
        s_array = [0] * (s_len + 1)
        s_array[0] = -1
        j = 0
        i = 1
        while i < s_len:
            if j == -1 or s[j] == s[i]:
                j += 1
                i += 1
                s_array[i] = j
            else:
                j = s_array[j]

        if s_array[-1] != 0 and s_array[-1] % (s_len - s_array[-1]) == 0:
            return True
        else:
            return False
