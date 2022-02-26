# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 21:22
# @Author  : Zhongyi Hua
# @File    : 220226_4.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res_list = []
        for cur1 in range(len(nums)-1):
            if nums[cur1] > 0:
                break
            if cur1 >= 1 and nums[cur1] == nums[cur1 - 1]:
                continue
            left = cur1 + 1
            right = len(nums) - 1
            while left < right:
                if nums[cur1] + nums[left] + nums[right] == 0:
                    res_list.append([nums[cur1], nums[left], nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif nums[cur1] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[cur1] + nums[left] + nums[right] < 0:
                    left += 1
        return res_list


