# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:24:49 2022

@author: romas
"""

import moving_equations as me

x = []

# <<<<<<< HEAD
def calculate_hit(t_start, t_end, delta_t, length, shoot_moment, velocity_shell, velocity_target, shoot_angle, height, g):

    t_1 = t_start

    hit = False

# =======
y = []

def calculate_hit(t_start, t_end, delta_t, length, shoot_moment, velocity_shell, velocity_target, shoot_angle, beta, height, g, x_start_shell, y_start_shell, x_start_target, y_start_target):

    t_1 = t_start

    hit = False

    time = []

# >>>>>>> parent of ca48d57 (Making it work as it should)
    shell_moving_x = []

    shell_moving_y = []

    target_moving_x = []

    target_moving_y = []
# <<<<<<< HEAD

    x_shell_t = 0

    y_shell_t = height

    x_target_t = 0

    y_target_t = length

    g = 9.81




    while t_1 <= t_end:


        x_shell_t, y_shell_t = me.shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, height, g)

        x_target_t, y_target_t = me.target_moving(length, velocity_target, t_1)

# =======

    x_shell_t = x_start_shell

    y_shell_t = y_start_shell

    x_target_t = x_start_target

    y_target_t = y_start_target


    while t_1 < t_end:

        time.append(t_1)

        # shell_moving_x.append(x_shell_t)

        # shell_moving_y.append(y_shell_t)

        # target_moving_x.append(x_target_t)

        # target_moving_y.append(y_target_t)



        # shell_move = me.shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, beta, height, g)

        # x_shell_t += shell_move[0]

        # y_shell_t += shell_move[1]

        x_shell_t, y_shell_t = me.shell_moving(t_1, shoot_moment, velocity_shell, shoot_angle, beta, height, g)


        # target_move = me.target_moving(length, velocity_target, t_1)

        # x_target_t += target_move[0]

        # y_target_t += target_move[1]

        x_target_t, y_target_t = me.target_moving(length, velocity_target, t_1)


# >>>>>>> parent of ca48d57 (Making it work as it should)
        shell_moving_x.append(x_shell_t)

        shell_moving_y.append(y_shell_t)

        target_moving_x.append(x_target_t)

        target_moving_y.append(y_target_t)

# <<<<<<< HEAD
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

# =======

        if round(x_shell_t) == round(x_target_t) and round(y_shell_t) == round(y_target_t):

            hit = True

            break

# >>>>>>> parent of ca48d57 (Making it work as it should)
        t_1 += delta_t

    return hit, t_1, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y

