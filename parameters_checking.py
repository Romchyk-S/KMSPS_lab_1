# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:02:49 2022

@author: romas
"""

def check_t_0(t_0, t_start, t_end):

    if t_0 < t_start or t_0 > t_end:

        t_0 = 10

    return t_0

def check_delta_t(t_0, t_start, t_end):

    if t_0 != 0:

        delta_t = (t_0/t_end)*10

    else:

        delta_t = (t_start-t_end) / 10

    return delta_t

def check_height_length(height, length):

    if height == 0:

        height += 10

    if length == 0:

        length += 10

    return height, length
