#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date: 2014-11-16 11:36:46
# @Last Modified by: Adrien Chardon
# @Last Modified time: 2014-11-16 12:41:08
 
from math import atan2, pi
 
 
def rondpoint(x, y, n, sorties):
    # calc angles for each way
    base_angle = atan2(sorties[0][1]-y, sorties[0][0]-x)
    angles = []
    for i in range(n):
        tmp_x = sorties[i][0]-x
        tmp_y = sorties[i][1]-y
        a = atan2(tmp_y, tmp_x) - base_angle
        if a < 0:
            a += 2*pi
        angles.append(a)

    # get the minimum
    index = 0
    min_angle = 2*pi
    for i in range(n):
        if (i != 0) and (angles[i] < min_angle):
            min_angle = angles[i]
            index = i
    
    return sorties[index][0], sorties[index][1]

if __name__ == "__main__":
    x, y = [int(i) for i in raw_input().split()]
    n = int(raw_input())
    sorties = [list(map(int, raw_input().split())) for _ in range(n)]
    print("%d %d" % rondpoint(x, y, n, sorties))
