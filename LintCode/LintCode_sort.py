# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:18:31 2019

@author: Administrator
"""

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        # 共有n-1个元素需要排 
        count = 0
        for i in range(n-1-j):
            # 对应j个元素比较的次数
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return alist
        print(alist)
            
    return alist
    
def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):
        #共有n-1个元素需要排
        min_index = j
        for i in range(1+j,n):
            # 对应第j个元素的比较次数
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
    return alist
        
def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(1,n):
        # 共需要插入n-1次
        for j in range(i-1,-1,-1):
            #和有序序列逐个比较
            if alist[j] > alist[i]:
                alist[j],alist[i] = alist[i],alist[j]
            else:
                break
    return alist  
        
def quick_sort(alist,start,end):
    """快速排序"""
    if start < end:
        i, j = start, end
        # 设置基数
        base = alist[i]
        while i < j:
            # 若后面的数>=base，则前移一位直到比基数小的出现
            while (i<j) and (alist[j]>=base):
                j -= 1
            alist[i] = alist[j]
            # 同样方式处理前半区
            while (i<j) and (alist[i]<=base):
                i += 1
            alist[j] = alist[i]
            
        # 第一轮循环做完，列表分为两个半区，且i=j，base设置回去
        alist[i] = base
        
        # 递归前后半区, i-1 和 i+1对应的索引值，不是range中的值
        quick_sort(alist,0,i-1) 
        quick_sort(alist,i+1,end)
    return alist

def merge_list(a,b):
    """合并两有序列表"""
    merged = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def merge_sort(alist):
    """归并排序，分治法"""
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    a = merge_sort(alist[:mid])
    b = merge_sort(alist[mid:])
    return merge_list(a,b)
    
    
    

if __name__ == '__main__':
    list = [11,2,5,21,33,9,0]
    print('bubble_sort',bubble_sort(list))
#    print('select_sort',select_sort(list))
#    print('insert_sort',insert_sort(list))
#    print('quick_sort ',quick_sort(list,0,6))
#    print('merge_sort ',merge_sort(list))
