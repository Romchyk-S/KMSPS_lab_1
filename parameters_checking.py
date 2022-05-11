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

    # неправильно виведено умови, відключив функцію

    summand_1 = ((velocity_shell/2)**2)*m.sin(2*shoot_angle)

    sqrt_parm = m.sqrt(((velocity_shell**2*m.sin(shoot_angle)**2)+2*g*height))

    if length*g < ((summand_1+(velocity_target*sqrt_parm))) or length*g < ((summand_1+(velocity_shell*m.cos(shoot_angle)*sqrt_parm))):

        return False

    return True

def get_t(velocity_shell, velocity_target, shoot_angle, height, length, g):

    l_v = (length/velocity_target)

    sqrt_parm = (velocity_shell*m.sin(shoot_angle))+(((velocity_shell**2*m.sin(shoot_angle)**2)+(2*g*height))**(1/2))

    divisor = velocity_target*g

    t_end = l_v - ((velocity_shell*m.cos(shoot_angle)*sqrt_parm)/divisor)

    t_0 = l_v - (((velocity_shell*m.cos(shoot_angle)+velocity_target)*sqrt_parm)/divisor)

    return t_end, t_0