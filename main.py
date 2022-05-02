# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""

import tkinter as tk

import trajectories_calculation as tc

import matplotlib.pyplot as plt

import matplotlib.animation as plta

import plots as p

import parameters_checking as pc

# import math as m


def animate(i):

    x_1.append(shell_moving_x[i])

    y_1.append(shell_moving_y[i])

    x_2.append(target_moving_x[i])

    y_2.append(target_moving_y[i])


    plt.plot(x_1, y_1, color = "orange")

    plt.plot(x_2, y_2, color = "blue")


t_start = 0

t_end = 100

t_0 = 4

v_0 = 6

v_1 = 5.6

l = 30

h = 10

alpha = 45


t_0 = pc.check_t_0(t_0, t_start, t_end)

delta_t = pc.check_delta_t(t_0, t_start, t_end)

h,l = pc.check_height_length(h, l)

hit, hit_moment, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y = tc.calculate_hit(t_start, t_end, delta_t, l, t_0, v_0, v_1, alpha, h)


x_1, y_1, x_2, y_2 = [], [], [], []


anim = plta.FuncAnimation(plt.gcf(), animate)

p.scatter_points(shell_moving_x, shell_moving_y, target_moving_x, target_moving_y)

plt.show()



if hit == True:

    print(f"Влучення відбулося в момент {hit_moment}")

else:

    print("Влучення не сталося")

