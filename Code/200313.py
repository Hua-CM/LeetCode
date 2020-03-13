# -*- coding: utf-8 -*-
# @Time : 2020/3/13 10:48
# @Author : Zhongyi Hua
# @FileName: 200313.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com


# 多数元素
class Solution:
    def majorityElement(self, nums):
        dict_1 = {}
        for key in nums:
            dict_1[key] = dict_1.get(key, 0) + 1
        for key, value in dict_1.items():
            if value > nums.__len__()/2:
                return key


# 和至少为K的最短子数组
class Solution2:
    def shortestSubarray(self, a, k):
        """
        :param a: 待处理数组
        :param k: K
        :return: 子数组长度
        """
        zhan = []
        for x in range(1, a.__len__()+1):
            zhan.append(sum(a[0:x]))

        for y in range(zhan.__len__()):
            y_zhan = zhan
            y_index_list = [x for x in range(zhan.__len__())]
            while y_zhan[y] > min(y_zhan[0:y]):
                y_zhan.pop(0)
                y_index_list.pop(0)
            while y_zhan[0] + k > y_zhan[index]:
                y_zhan.pop()




