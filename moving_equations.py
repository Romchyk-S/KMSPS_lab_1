# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:38:22 2022

@author: romas
"""

import math as m

def shell_moving(t, shoot_moment, velocity, angle, height, g):

    # для руху з опором повітря, можна спробувати дописати

    # exponent = 1-m.exp(-beta*(t-shoot_moment))

    # relation = velocity/beta

    # x = (relation * m.cos(angle)) * exponent

    # y = (relation * m.sin(angle) + (g/m.pow(beta, 2))) * (1-m.exp(-beta*(t-shoot_moment))) - ((g/beta)*(t-shoot_moment)) + height

   if t-shoot_moment < 0:

       x = 0

       y = height

   else:

       x = round(velocity*m.cos(angle)*(t-shoot_moment), 6)

       y = round((-g/2)*((t-shoot_moment)**2) + velocity*m.sin(angle)*(t-shoot_moment) + height, 6)

   return x, y

def target_moving(length, velocity, t):

    x = round(length-velocity*t, 6)

    y = 0

    return x, y


def calculate_hit(t_start, t_end, delta_t, length, shoot_moment, velocity_shell, velocity_target, shoot_angle, height, g):

    t_1 = t_start

    hit = False

    shell_moving_x, shell_moving_y, target_moving_x, target_moving_y = [], [], [], []

    x_shell_t, y_shell_t = 0, height

    x_target_t, y_target_t = 0, length



    i = 0

    end = False


    while t_1 <= t_end:

        x_shell_t, y_shell_t = shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, height, g)

        x_target_t, y_target_t = target_moving(length, velocity_target, t_1)


        if i%100 == 0 or t_1 == t_end:

            shell_moving_x.append(x_shell_t)

            shell_moving_y.append(y_shell_t)

            target_moving_x.append(x_target_t)

            target_moving_y.append(y_target_t)


        if t_1 + delta_t <= t_end or end == True:

            t_1 += delta_t

        elif end == False:

            t_1 = t_end

            end = True

        i += 1


    return hit, t_1, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y
