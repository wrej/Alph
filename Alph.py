#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:17:03 2022

@author: wojciechrejdak
"""
s = input('Enter your string here:')

l = []
for i in range(len(s)):
    for j in range(len(s)+1):
        if j <= i:
            continue
        else:
            s1 = s[i:j]
            sb = ''
            sb = sb.join(sorted(s1))
            if s1 == sb:
                l.append(sb)
print('Longest substring in alphabetical order is: '+
      max(l, key=len))