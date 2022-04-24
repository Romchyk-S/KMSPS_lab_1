# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:38:22 2022

@author: romas
"""

import math as m

def shell_moving(t, shoot_moment, velocity, angle, beta, height, g):
    
    x = (velocity/beta) * m.cos(angle) * (1-m.exp(-beta*(t-shoot_moment)))
    
    y = ((velocity/beta) * m.sin(angle) + (g/m.pow(beta, 2))) * (1-m.exp(-beta*(t-shoot_moment))) - (g/beta*(t-shoot_moment) + height)
    
    return x, y

def target_moving(length, velocity, t):
    
    x = length-velocity*t
    
    y = 0
    
    return x, y
