# -*- coding: utf-8 -*-
# @Time : 2022/3/12 1:40
# @Author : Zhongyi Hua
# @FileName: 220312.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        count_ = 0
        cur_l = 0
        cur_r = 0
        while cur_r < len(nums):
            if nums[cur_r] != val:
                nums[cur_r], nums[cur_l] = nums[cur_l], nums[cur_r]
                cur_r += 1
                cur_l += 1
                count_ += 1
            else:
                cur_r += 1
        return count_
