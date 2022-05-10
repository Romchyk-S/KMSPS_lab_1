# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:24:49 2022

@author: romas
"""

import moving_equations as me


def calculate_hit(t_start, t_end, delta_t, length, shoot_moment, velocity_shell, velocity_target, shoot_angle, height, g):

    t_1 = t_start

    hit = False

    shell_moving_x = []

    shell_moving_y = []

    target_moving_x = []

    target_moving_y = []

    x_shell_t = 0

    y_shell_t = height

    x_target_t = 0

    y_target_t = length


    while t_1 <= t_end:


        x_shell_t, y_shell_t = me.shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, height, g)

        x_target_t, y_target_t = me.target_moving(length, velocity_target, t_1)

        shell_moving_x.append(x_shell_t)

        shell_moving_y.append(y_shell_t)

        target_moving_x.append(x_target_t)

        target_moving_y.append(y_target_t)

        # x_shell_comparison = round(x_shell_t)

        # y_shell_comparison = round(y_shell_t)

        # x_target_comparison = round(x_target_t)

        # y_target_comparison = round(y_target_t)


        if round(y_shell_t, 1) <= 0:

            break


        # if x_shell_comparison == x_target_comparison and y_shell_comparison == y_target_comparison:

        #     print(f"{round(x_shell_t, 1)};{round(y_shell_t, 1)}")

        #     print(f"{round(x_target_t, 1)};{round(y_target_t, 1)}")

        #     print()

        #     hit = True

        #     break

        t_1 += delta_t

    return hit, t_1, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y

