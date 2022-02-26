# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 20:51
# @Author  : Zhongyi Hua
# @File    : 220226_3.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        query_dict = {v: k for k, v in enumerate(nums)}
        for val, idx in query_dict.items():
            if target - val in query_dict:
                if val == target - val:
                    continue
                else:
                    return [idx, query_dict.get(target - val)]
        return [k for k, v in enumerate(nums) if v == target/2]
