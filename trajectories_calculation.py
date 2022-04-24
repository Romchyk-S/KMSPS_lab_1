# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:24:49 2022

@author: romas
"""

import moving_equations as me

def calculate_hit(t_start, t_end, delta_t, length, shoot_moment, velocity_shell, velocity_target, shoot_angle, beta, height, g):
    
    t_1 = t_start

    hit = False
    
    time = []
    
    
    while t_1 < t_end:
        
        time.append(t_1)
        
        x_shell_t, y_shell_t = me.shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, beta, height, g)
        
        x_target_t, y_target_t = me.target_moving(length, velocity_target, t_1)
        
        if x_shell_t == x_target_t and y_shell_t == y_target_t:
            
            hit = True
            
            break
        
        t_1 += delta_t
        
    return hit, t_1