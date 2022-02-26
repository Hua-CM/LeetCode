# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 17:46
# @Author  : Zhongyi Hua
# @File    : 220226.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for _ in list(s):
            record[ord(_) - ord('a')] += 1
        for _ in list(t):
            record[ord(_) - ord('a')] -= 1
        if record == [0] * 26:
            return True
        else:
            return False

