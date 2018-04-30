# -*- coding: utf-8 -*-
# 思路来自 https://blog.csdn.net/ice_camel/article/details/44263451
string = input()
list = list(string)  
list.reverse()  
T = 0
AT = 0
PAT = 0
for num in list:  
    if 'T' == num:  
        T += 1
    elif 'A' == num:  
        AT += T
    else:  
        PAT +=AT
print(PAT%1000000007)