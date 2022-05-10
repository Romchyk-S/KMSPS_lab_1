# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""

# import tkinter as tk

import moving_equations as me

import matplotlib.pyplot as plt

import matplotlib.animation as plta

import plots as p

import parameters_checking as pc


def animate(i):

    x_1.append(shell_moving_x[i])

    y_1.append(shell_moving_y[i])

    x_2.append(target_moving_x[i])

    y_2.append(target_moving_y[i])


    plt.plot(x_1, y_1, color = "orange")

    plt.plot(x_2, y_2, color = "blue")



# ці параметри можна змінювати та дивитися, який вийде результат

v_0 = 6

v_1 = 12

l = 30

h = 10

alpha = 45


t_start = 0

delta_t = 0.05

g = 9.81



t_end, t_0 = pc.get_t(v_0, v_1, alpha, h, l, g)

if pc.check_t_not_negative(v_0, v_1, alpha, h, l, g):

    h,l = pc.check_height_length(h, l)

    t_end, t_0 = pc.get_t(v_0, v_1, alpha, h, l, g)

    print(f"Момент пострілу: {t_0}")

    print(f"Момент влучення: {t_end}")

    print()


    hit, hit_moment, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y = me.calculate_hit(t_start, t_end, delta_t, l, t_0, v_0, v_1, alpha, h, g)

    print("Координати влучення:")

    print(f"Снаряд: ({shell_moving_x[-1]};{shell_moving_y[-1]})")

    print(f"Мішень: ({target_moving_x[-1]};{target_moving_y[-1]})")


    x_1, y_1, x_2, y_2 = [], [], [], []

    anim = plta.FuncAnimation(plt.gcf(), animate)

    p.scatter_points(shell_moving_x, shell_moving_y, target_moving_x, target_moving_y)

    plt.show()

else:

    print()

    print("Умови додатності часу не виконано")

