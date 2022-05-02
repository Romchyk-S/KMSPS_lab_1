# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:00:14 2022

@author: romas
"""

import matplotlib.pyplot as plt

def scatter_points(shell_move_x, shell_move_y, target_move_x, target_move_y):

    plt.scatter(shell_move_x[0], shell_move_y[0], color = 'orange')

    plt.scatter(target_move_x[0], target_move_y[0], color = 'blue')

    plt.scatter(shell_move_x[-1], shell_move_y[-1], color = 'orange')

    plt.scatter(target_move_x[-1], target_move_y[-1], color = 'blue')

