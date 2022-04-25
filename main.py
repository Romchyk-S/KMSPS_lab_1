# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:30:13 2022

@author: romas
"""



import tkinter as tk

import trajectories_calculation as tc

import matplotlib.pyplot as plt

import matplotlib.animation as plta

import math as m


t_start = 0

t_end = 10

g = 9.81

time = []


t_0 = 4

if t_0 < t_start or t_0 > t_end:
    
    t_0 = 10
    
    

if t_0 != 0:

    delta_t = t_0/t_end
    
else:
    
    delta_t = (t_start-t_end) / 10
    
    

v_0 = 2

v_1 = 1

l = 10

h = 10

alpha = 10

beta = 0

x_0 = 0

y_0 = h

x_1 = l

y_1 = 0


if h == 0:
    
    h += 10
    
if l == 0:
    
    l += 10
    
    
hit, hit_moment, shell_moving_x, shell_moving_y, target_moving_x, target_moving_y = tc.calculate_hit(t_start, t_end, delta_t, l, t_0, v_0, v_1, alpha, beta, h, g, x_0, y_0, x_1, y_1)

x_1 = []

y_1 = []

x_2 = []

y_2 = []



def animate(i):
    
    x_1.append(shell_moving_x[i])
    
    y_1.append(shell_moving_y[i])
    
    x_2.append(target_moving_x[i])
    
    y_2.append(target_moving_y[i])
    
    
    plt.plot(x_1, y_1, color = "orange")
    
    plt.plot(x_2, y_2, color = "blue")


anim = plta.FuncAnimation(plt.gcf(), animate)

plt.show()


if hit == True:
    
    print(f"Влучення відбулося в момент {hit_moment}")
    
else:
    
    print("Влучення не сталося")

    
plt.scatter(shell_moving_x[0], shell_moving_y[0], color = 'orange')

plt.scatter(target_moving_x[0], target_moving_y[0], color = 'blue')

# plt.scatter(shell_moving_x[5], shell_moving_y[5], color = 'orange')

# plt.scatter(target_moving_x[5], target_moving_y[5], color = 'blue')

plt.show()
