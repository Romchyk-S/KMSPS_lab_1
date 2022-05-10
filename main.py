# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""

# import tkinter as tk

import trajectories_calculation as tc

import matplotlib.pyplot as plt

import matplotlib.animation as plta

import plots as p

import parameters_checking as pc

import math as m


def animate(i):

    x_1.append(shell_moving_x[i])

    y_1.append(shell_moving_y[i])

    x_2.append(target_moving_x[i])

    y_2.append(target_moving_y[i])


    plt.plot(x_1, y_1, color = "orange")

    plt.plot(x_2, y_2, color = "blue")



v_0 = 6

v_1 = 10

l = 30

h = 10

alpha = 60


t_start = 0

g = 9.81

# sqr_parm = (v_0*m.sin(alpha))+(((v_0**2*m.sin(alpha)**2)+(2*g*h))**(1/2))

# t_end = (l/v_1)-((v_0*m.cos(alpha)*sqr_parm)/(v_1*g))

# t_0 = (l/v_1)-(((sqr_parm)*(v_0*m.cos(alpha)+v_1))/(v_1*g))

t_0 = 4

t_end = 100

print(t_0)

print(t_end)

t_0 = pc.check_t_0(t_0, t_start, t_end)


h,l = pc.check_height_length(h, l)

delta_t = pc.get_delta_t(t_0, t_start, t_end)


hit, hit_moment, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y = tc.calculate_hit(t_start, t_end, delta_t, l, t_0, v_0, v_1, alpha, h, g)

if hit == True:

    print(f"Влучення відбулося в момент {hit_moment}")

else:

    print("Влучення не сталося")


print(f"({shell_moving_x[-1]};{shell_moving_y[-1]})")

print(f"({target_moving_x[-1]};{target_moving_y[-1]})")


x_1, y_1, x_2, y_2 = [], [], [], []

anim = plta.FuncAnimation(plt.gcf(), animate)

p.scatter_points(shell_moving_x, shell_moving_y, target_moving_x, target_moving_y)

plt.show()

