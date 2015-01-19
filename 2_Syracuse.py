#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date: 2014-11-16 12:44:31
# @Last Modified by: Adrien Chardon
# @Last Modified time: 2014-11-16 12:44:52


def syracuse(u0, k):
    for i in range(k):
        if u0 % 2 == 0:
            u0 = u0/2
        else:
            u0 = u0*3+1
    return int(u0)
 
 
if __name__ == '__main__':
    u0 = int(raw_input())
    k = int(raw_input())
    print(syracuse(u0, k))
