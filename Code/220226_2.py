# -*- coding: utf-8 -*-
# @Time    : 2022/2/26 17:58
# @Author  : Zhongyi Hua
# @File    : 220226_2.py
# @Usage   :
# @Note    : 
# @E-mail  : njbxhzy@hotmail.com

class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        def recursion(_n, _record):
            _record.add(_n)
            _m = 0
            for _ in list('%d' % _n):
                _m += int(_) * int(_)
            if _m == 1:
                return True
            elif _m in _record:
                return False
            else:
                return recursion(_m, _record)

        return recursion(n, record)
