# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:02:49 2022

@author: romas
"""

import math as m

def check_t_0(t_0, t_start, t_end):

    if t_0 < t_start or t_0 > t_end:

        t_0 = (t_0-t_end) / 2

    return t_0

def check_height_length(height, length):

    if height == 0:

        height += 10

    if length == 0:

        length += 10

    return height, length

def check_t_not_negative(velocity_shell, velocity_target, shoot_angle, height, length, g):

    summand_1 = velocity_shell**2*m.sin(2*shoot_angle)

    sqrt_parm = 2*(velocity_shell*m.sin(shoot_angle)**2+2*g*height)**(1/2)

    divisor = 2*g

    if length <= (summand_1+(velocity_target*sqrt_parm))/divisor or length <= (summand_1+(velocity_shell*m.cos(shoot_angle)*sqrt_parm))/divisor:

        return False

    return True

def get_t(velocity_shell, velocity_target, shoot_angle, height, length, g):

    sqrt_parm = (velocity_shell*m.sin(shoot_angle))+(((velocity_shell**2*m.sin(shoot_angle)**2)+(2*g*height))**(1/2))\

    t_end = (length/velocity_target)-((velocity_shell*m.cos(shoot_angle)*sqrt_parm)/(velocity_target*g))

    t_0 = (length/velocity_target)-(((sqrt_parm)*(velocity_shell*m.cos(shoot_angle)+velocity_target))/(velocity_target*g))

    return t_end, t_0