# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:51:24 2022

@author: romas
"""

import tkinter as tk


def button_func(arr_entr, arr_var, root):

    i = 0

    while i < len(arr_entr):

        try:

            arr_var.append(float(arr_entr[i].get()))

        except ValueError:

            root_1 = tk.Tk()

            root_1.title("ПОМИЛКА")

            root_1.minsize(400, 100)

            label = tk.Label(root_1, text = "Не всі параметри є числом.")

            label.pack()

        i += 1

    root.destroy()


def make_interface():

    root = tk.Tk()

    root.title("Параметри системи")

    root.minsize(600, 400)

    entry_arr = []

    label_1, entry_1 = create_label_entry("v_0: ", root)

    entry_1.insert(tk.END, "5")

    pack_label_entry(entry_arr, label_1, entry_1)


    label_2, entry_2 = create_label_entry("v_1: ", root)

    entry_2.insert(tk.END, "12")

    pack_label_entry(entry_arr, label_2, entry_2)


    label_3, entry_3 = create_label_entry("l: ", root)

    entry_3.insert(tk.END, "30")

    pack_label_entry(entry_arr, label_3, entry_3)


    label_4, entry_4 = create_label_entry("h: ", root)

    entry_4.insert(tk.END, "10")

    pack_label_entry(entry_arr, label_4, entry_4)


    label_5, entry_5 = create_label_entry("alpha: ", root)

    entry_5.insert(tk.END, "45")

    pack_label_entry(entry_arr, label_5, entry_5)

    variables = []

    submit_button = tk.Button(root, text='Задати параметри', command = lambda: button_func(entry_arr, variables, root))

    submit_button.pack()

    root.mainloop()

    return variables

def create_label_entry(text, root):

    label = tk.Label(root, text=text)

    entry = tk.Entry(root)

    return label, entry

def pack_label_entry(entries_arr, label, entry):

    label.pack()

    entry.pack()

    entries_arr.append(entry)