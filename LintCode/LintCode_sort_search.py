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

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if len(alist) <= 1:
        return alist
    mid = n // 2
    # left right 采用归并排序形成新的列表
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并成新的序列，merge(left,right)
    result = []
    left, right =0, 0
    while left<len(left_li) and right<len(right_li):
        if left_li[left] <= right_li[right]:
            result.append(left_li[left])
            left += 1
        else:
            result.append(right_li[right])
            right += 1

    result.extend(left_li[left:])
    result.extend(right_li[right:])
    return result

"""
分析 merge_sort 中的归并过程
merge_sort [11,2,5,21,33,9,0]
left_li = merge_sort [11,2,5] --> [2,5,11]
    left_li = merge_sort[11] --> [11]
    right_li = [2,5]
     #right_li = merge_sort [2,5]
     #left_li = merge_sort [2] --> [2]
     #rigt_li = merge_sort [5] --> [5]
     #return reslut -->[2,5]
    return result -->[2,5,11]
right_li = merge_sort[21,33,9,0] -->[0,9,21,33]
    .....
    .....
return result [0, 2, 5, 9, 11, 21, 33]
"""

def binary_search(alist,value):
    """二分查找，递归"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == value:
            return value
        elif value < alist[mid]:
            return binary_search(alist[0:mid],value)
        else:
            return binary_search(alist[mid+1:],value)
    return False

def binary_search_2(alist,value):
    """二分查找，非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == value:
            return value
        elif value < alist[mid]:
            last = mid -1
        else:
            first = mid + 1
    return False





if __name__ == '__main__':
    list = [1,3,4,5,6,9,11,44]
    print(binary_search(list,90))
    print(binary_search_2(list,90))

