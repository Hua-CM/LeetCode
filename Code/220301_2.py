# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 14:54
# @Author  : Zhongyi Hua
# @File    : 220301_2.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = [0] * 26
        start_val = ord('a')
        for _ in list(magazine):
            magazine_list[ord(_) - start_val] += 1
        ransom_list = [0] * 26
        for _ in list(ransomNote):
            ransom_list[ord(_) - start_val] += 1
        for i in range(26):
            if ransom_list[i] > magazine_list[i]:
                return False
        return True
