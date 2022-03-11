# -*- coding: utf-8 -*-
# @Time : 2022/3/8 0:31
# @Author : Zhongyi Hua
# @FileName: 220308.py
# @Usage: 
# @Note:
# @E-mail: njbxhzy@hotmail.com

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_array = list(needle)
        haystack_array = list(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0

        # generate next array
        next_array = [0] * (needle_len)
        next_array[0] = -1
        left = -1
        right = 0
        while right < needle_len-1:
            if left == -1 or needle_array[right] == needle_array[left]:
                left += 1
                right += 1
                next_array[right] = left # 因为记录的实际上是前一个都值，所以先加再记
            else:
                left = next_array[left]

        # match
        idx = 0
        idx2 = 0
        while idx <= len(haystack_array) - 1:
            if idx2 == -1 or haystack_array[idx] == needle_array[idx2]:
                idx += 1
                idx2 += 1
            else:
                idx2 = next_array[idx2]
            if idx2 == needle_len:  # summed in line 34
                return idx - needle_len
        return -1
