#!/usr/bin/python3

def uniq_add(my_list=[]):
    ans = 0
    for x in set(my_list):
        ans += x
    return ans
