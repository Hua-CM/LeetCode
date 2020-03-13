# -*- coding: utf-8 -*-
# @Time : 2020/3/13 10:48
# @Author : Zhongyi Hua
# @FileName: 200313.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com


class Solution:
    def majorityElement(self, nums):
        dict_1 = {}
        for key in nums:
            dict_1[key] = dict_1.get(key, 0) + 1
        for key, value in dict_1.items():
            if value > nums.__len__()/2:
                return key