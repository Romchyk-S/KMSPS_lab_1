# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""

import math as m

import tkinter as tk



t_start = 0

t_end = 100

g = 9.81



t_0 = 0

v_0 = 0

v_1 = 0

l = 0

h = 0

alpha = 0

beta = 0



def shell_moving(t, t_0, velocity, angle, beta, height):
    
    x = (velocity/beta) * m.cos(angle) * (1-m.exp(-beta*(t-t_0)))
    
    y = ((velocity/beta) * m.sin(angle) + (g/m.pow(beta, 2))) * (1-m.exp(-beta*(t-t_0))) - (g/beta*(t-t_0) + height)
    
    return x, y

def target_moving(length, velocity, t):
    
    x = l-velocity*t
    
    y = 0
    
    return x, y