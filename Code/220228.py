# -*- coding: utf-8 -*-
# @Time : 2022/3/1 1:02
# @Author : Zhongyi Hua
# @FileName: 220228.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res_list = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        res_list.add((nums[i], nums[j], nums[left], nums[right]))
                        while left != right and nums[left] == nums[left + 1]:
                            left += 1
                        while left != right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
        return [list(_) for _ in list(res_list)]
