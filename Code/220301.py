# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 14:30
# @Author  : Zhongyi Hua
# @File    : 220301.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        a = defaultdict(int)
        for _ in nums1:
            for __ in nums2:
                a[_ + __] += 1
        count = 0
        for c in nums3:
            for d in nums4:
                count += a.get(0 - c - d, 0)
        return count
