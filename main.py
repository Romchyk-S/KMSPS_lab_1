# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""



import tkinter as tk

import trajectories_calculation as tc



t_start = 0

t_end = 100

delta_t = 10

g = 9.81

time = []


t_0 = 10

v_0 = 10

v_1 = 5

l = 10

h = 10

alpha = 0

beta = 1


if h == 0:
    
    h += 10
    
if l == 0:
    
    l += 10
    

hit, hit_moment = tc.calculate_hit(t_start, t_end, delta_t, l, t_0, v_0, v_1, alpha, beta, h, g)

if hit == True:
    
    print(f"Влучення відбулося в момент {hit_moment}")
    
else:
    
    print("Влучення не сталося")