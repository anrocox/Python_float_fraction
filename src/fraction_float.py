#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to represent a float in a fraction in Python?

¿Cómo representar un float en una fracción en Python?
'''

#create a float number
f = 4.5
print(f)

#this method generates a tuple with two integers, the first is the numerator
#and the second is the positive denominator.
t = f.as_integer_ratio()
print(type(t))
print(t)

#create a negative number
f = -12.25
print(f)

#generate the fraction that represent the float number
t = f.as_integer_ratio()
print(t)
