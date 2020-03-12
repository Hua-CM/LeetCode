# -*- coding: utf-8 -*-
# @Time : 2020/3/12 11:21
# @Author : Zhongyi Hua
# @FileName: 200312.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com


class Solution(object):
    def gcdOfStrings(self, str1: str, str2: str):
        def ojld(value1, value2):
            mod_value = 1
            while not mod_value ==0:
                mod_value = value1 % value2
                value1 = value2
                if not mod_value == 0:
                    value2 = mod_value
                else:
                    return value2
        value1 = max(str1.__len__(), str2.__len__())
        value2 = min(str1.__len__(), str2.__len__())
        num = int(ojld(value1, value2))
        max_str = str1[0:num]
        if max_str*int(str1.__len__()/num) == str1 and max_str*int(str2.__len__()/num) == str2:
            return max_str
        else:
            return ""
