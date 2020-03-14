# -*- coding: utf-8 -*-
# @Time : 2020/3/14 11:29
# @Author : Zhongyi Hua
# @FileName: 200314.py
# @Usage: z
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums.__len__() == 0:
            return 0
        elif nums.__len__() == 1:
            return 1
        else:
            dp = []
        for i in range(nums.__len__()):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

