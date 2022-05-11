# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""

import moving_equations as me

import matplotlib.pyplot as plt

import matplotlib.animation as plta

import plots as p

import parameters_checking as pc

import math as m

import interface as inter


print()


def animate(i):

    x_1.append(shell_moving_x[i])

    y_1.append(shell_moving_y[i])

    x_2.append(target_moving_x[i])

    y_2.append(target_moving_y[i])


    plt.plot(x_1, y_1, color = "orange")

    plt.plot(x_2, y_2, color = "blue")



variables = inter.make_interface()

try:

    v_0, v_1, l, h, alpha = variables[0], variables[1], variables[2], variables[3], m.radians(variables[4])

    print("Параметри системи:")

    print(f"v_0 = {v_0}")

    print(f"v_1 = {v_1}")

    print(f"l = {l}")

    print(f"h = {h}")

    print(f"alpha = {m.degrees(alpha)}")

    print()


    t_start = 0

    delta_t = 0.001

    g = 9.81



    t_end, t_0 = pc.get_t(v_0, v_1, alpha, h, l, g)

    print(f"Момент пострілу: {t_0}")

    print(f"Момент влучення: {t_end}")

    print()



    if t_0 >= 0 and t_end >= 0:

        h,l = pc.check_height_length(h, l)

        t_end, t_0 = pc.get_t(v_0, v_1, alpha, h, l, g)


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

except:

    print("Виникла неочікувана помилка, можливо введено неправильні дані.")
