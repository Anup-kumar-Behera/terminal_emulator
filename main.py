import sys
import math as m
import os
import tkinter as tk
from tkterminal import Terminal
from tkinter import ttk
import time


def create_tabbed_window(no_of_terminals, commands):
    no_of_tabs = m.ceil(int(no_of_terminals)/4)
    # print(no_of_tabs)
    cwd = os.getcwd()
    print(cwd)
    terminal_name = 'tkterminal$'
    terminal_name = cwd.split('/')[-1:][0] + '$'
    root = tk.Tk()
    root.title("Tab Widget")
    tabControl = ttk.Notebook(root)
    command_index = 0
    if len(commands) <= 0:
        command_index = -1
    for tab in range(no_of_tabs):
        terminals = 0
        if tab == no_of_tabs - 1 and no_of_terminals % 4 != 0:
            terminals = no_of_terminals % 4
        else:
            terminals = 4

        taab = ttk.Frame(tabControl)

        # tabControl.add(tab1, text ='Tab 1')
        tabControl.add(taab, text = 'tab' + str(tab))
        tabControl.pack(expand=1, fill="both")


        for terminal in range(terminals):
            cmd = ''
            if command_index >= 0 and command_index < len(commands):
                cmd = commands[command_index]
                command_index += 1
            if len(cmd) > 0:
                tmp1 = cmd.split(';')
                if len(tmp1) > 0:
                    tmp1 = tmp1[0].split(' ')
                    if len(tmp1) > 1:
                        terminal_name = tmp1[1] + '$'

            if terminal == 0:
                h, w = 30, 80
                t = ''
                if terminals == 1:
                    h, w = 60, 200
                elif terminals == 2:
                    h, w = 60, 100
                if terminals != 1:
                    t = Terminal(taab,background='black', foreground='white', width = w, height = h)
                else:
                    t = Terminal(taab, width = w, height = h)

                t.grid(row = 0, column = 0, sticky="news")
                t.shell = True
                t.basename = terminal_name
                command = cwd
                t.run_command('cd ' + command +'; ' + cmd)
                # time.sleep(5)

            elif terminal == 1:
                h, w = 30, 100
                if terminals == 2:
                    h, w = 60, 100
                t = Terminal(taab, width=w, height=h)
                t.grid(row=0, column=1, sticky="news")
                t.shell = True
                t.basename = terminal_name
                command = cwd
                t.run_command('cd ' + command + '; '+cmd)
                # time.sleep(5)

            elif terminal == 2:
                t = Terminal(taab, width=100, height=30)
                t.grid(row=1, column=0, sticky="news")
                t.shell = True
                t.basename = terminal_name
                command = cwd
                t.run_command('cd ' + command + '; ' + cmd)
                # time.sleep(5)

            else:
                t = Terminal(taab, background='black', foreground='white', width=100, height=30)
                t.grid(row=1, column=1, sticky="news")
                t.shell = True
                t.basename = terminal_name
                command = cwd
                t.run_command('cd ' + command + '; ' + cmd)
                # time.sleep(5)

    root.mainloop()


if __name__ == '__main__':
    n = len(sys.argv)
    no_of_terminals = int(sys.argv[1])
    commands = sys.argv[2:]

    create_tabbed_window(no_of_terminals, commands)

    # print(commands)


