# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:30:01 2019

@author: Administrator
"""
# 动态规划的三要素:最优子结构,边界和状态转移函数

# 爬楼梯.假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。
#你有多少种不同的方法可以爬到楼顶呢？

class Solution(object):
    def climb_stairs(self,n):
        """爬楼梯
        para n: 共有n阶
        return：所有方法"""
        if n <= 2:
            return n
        f_1 = 1 #边界
        f_2 = 2 #边界
        for i in range(3,n+1):
            f = f_1 + f_2 #状态转移
            f_2 = f_1  #最优子结构
            f_1 = f    #最优子结构
        return f

if __name__ == '__main__':
    solution = Solution()
    print(solution.climb_stairs(10))


