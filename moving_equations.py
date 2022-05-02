# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:38:22 2022

@author: romas
"""

import math as m

def shell_moving(t, shoot_moment, velocity, angle, height, g):

    # exponent = 1-m.exp(-beta*(t-shoot_moment))

    # relation = velocity/beta

    # x = (relation * m.cos(angle)) * exponent

    # y = (relation * m.sin(angle) + (g/m.pow(beta, 2))) * (1-m.exp(-beta*(t-shoot_moment))) - ((g/beta)*(t-shoot_moment)) + height

   if t-shoot_moment < 0:

       x = 0

       y = height

   else:

       x = velocity*m.cos(angle)*(t-shoot_moment)

       y = -g*((t-shoot_moment)**2) + velocity*m.sin(angle)*(t-shoot_moment) + height

   return x, y

def target_moving(length, velocity, t):

    x = length-velocity*t

    y = 0

    return x, y
