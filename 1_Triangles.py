#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# @Author: Adrien Chardon
# @Date: 2014-11-16 12:43:39
# @Last Modified by: Adrien Chardon
# @Last Modified time: 2014-11-16 12:44:11

def triangles(n):
    return int(n*(n+1)/2)

if __name__ == '__main__':
    print(triangles(int(raw_input())))
