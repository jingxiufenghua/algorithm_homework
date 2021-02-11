import pandas as pd
import numpy as np

#将List分为两部分，并返回切分好的2个list和切分的位置信息
def divide_two_part(a):
    pivot = len(a)//2
    part_first = a[0:pivot]
    part_two = a[pivot:]
    return part_first,part_two


"""
对于给出的两个有序列表判断数据是否为逆序数，第一次是两个数据所以无所谓是否顺序，
但是返回的时候是顺序列表，后面递归调用的时候，传入的参数就是上一次返回的顺序的列表了
"""
def is_reverse(a,b):
    count = 0
    list_resort = []
    list_out = []
    a_len = len(a)
    b_len = len(b)
    flag_a = 0  # A 游标
    flag_b = 0  # B 游标
    for i in range(flag_a,a_len):
        for j in range(flag_b,b_len):
            if b[j]<a[i]:
                count= count+a_len-flag_a   # b[j]<a[i]  那么 b[j] 小于 a[flag_a] 到a[len(a)]的所有数据
                list_resort.append(b[j])
                for t in range(flag_a,a_len): # 提取逆序数对
                    temp = [a[t],b[j]]
                    list_out.append(temp)
                flag_b = flag_b + 1  # 数组b下标右移
                continue
            else:
                list_resort.append(a[i])
                flag_a = flag_a + 1  # 数组a下标右移
                break
        if flag_b==b_len :
            list_resort = list_resort + a[i:]
            break
        if i==a_len-1 :
            list_resort = list_resort + b[j:]
            break
    return list_resort,count,list_out     #返回顺序列表，逆序数对个数，逆序数对



#利用递归的方式
def count_reverse(given_list):
    list_a,list_b = divide_two_part(given_list)
    if len(list_a)>=2 or len(list_b)>=2:
        list_resort_a, count_a,list_out_a = count_reverse(list_a)
        list_resort_b, count_b,list_out_b = count_reverse(list_b)
        list_resort,count_conquer,list_out_a_b= is_reverse(list_resort_a,list_resort_b)
        count = count_a + count_b + count_conquer
        list_out = list_out_a + list_out_b+list_out_a_b
        return list_resort,count,list_out
    else:
        list_resort,count,list_out = is_reverse(list_a,list_b)
        return  list_resort,count,list_out


a = [11, 0, -14, -7, 17, -2, 16, 22]

list_resort,count,list_out = count_reverse(a)
print("逆序数对:",list_out,"\n","逆序数个数",count,"\n","顺序列表",list_resort)

