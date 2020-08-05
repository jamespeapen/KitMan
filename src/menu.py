'''
Curses-based menu for the KitMan TUI
Created Aug 04 2020
Author: James Eapen (jamespeapen@gmail.com)
'''

import curses
import pyfiglet


class Menu:

    def __init__(self):
        self.screen = curses.initscr()
        self.n_rows, self.n_cols = self.screen.getmaxyx()

    def draw_banner(self):
        center_col = int(self.n_cols/2)
        self.screen.addstr(1, 1, pyfiglet.figlet_format("KitMan"))
        self.screen.refresh()

menu = Menu()
menu.draw_banner()
