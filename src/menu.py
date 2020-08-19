'''
Curses-based menu for the KitMan TUI
Created Aug 04 2020
Author: James Eapen (jamespeapen@gmail.com)
'''

from data_operations import Data
from kitchen import Kitchen
import curses
import pyfiglet
import time

class Menu:

    def __init__(self):

        self.data = Data()
        self.kitchen = Kitchen()
        self.kitchen.pantry = self.data.read_pantry('test/test_read_pantry.json')
        self.kitchen.recipies = self.data.read_recipies('test/test_read_recipies.json')

        self.stdscr = curses.initscr()
        self.height, self.width = self.stdscr.getmaxyx()

        # windows
        self.menubar = curses.newwin(2, self.width, 0, 0)

        self.data_window = curses.newwin(self.height-3,
                                         2 * (self.width // 3), 3, 0)

        self.preview_window = curses.newwin(self.height - 3,
                                            self.width // 3, 4,
                                            2 * (self.width // 3))

    def menu(self, stdscr, current_row):

        menu_bar = ["1: Pantry",
                    "2: Recipies",
                    "3: Shopping"]

        y = 0
        x = 1

        for idx, element in enumerate(menu_bar):

            self.menubar.addstr(y, x, element)
            x += len(element) + len(menu_bar) // (len(menu_bar) - 1)

        self.menubar.refresh()

    def pantry(self, stdscr):

        self.data_window.clear()

        self.data_window.addstr(0, 0, "Food\tQuantity in stock")
        y = 2
        x = 0

        for food in self.kitchen.pantry:
            self.data_window.addstr(y, x, food + '\t' + str(self.kitchen.pantry[food]))
            y += 2

        self.data_window.refresh()

    def recipies(self, stdscr):

        self.data_window.clear()
        self.data_window.addstr(0, 0, "Recipies")
        y = 2
        x = 0

        for recipie in self.kitchen.recipies:
            self.data_window.addstr(y, x, recipie.name)
            y += 2
        self.data_window.refresh()

    def main(self, stdscr):

        curses.curs_set(0)

        current_row = 0

        self.menu(self.stdscr, current_row)

        while True:
            key = self.stdscr.getch()

            if key == ord('1'):
                self.pantry(stdscr)

            elif key == ord('2'):
                self.recipies(stdscr)
#
#            if (key == curses.KEY_UP or key == ord("k")) and current_row > 0:
#                current_row -= 1
#
#            elif (key == curses.KEY_DOWN or key == ord("j")) \
#            and current_row < len(self.menu_list) - 1:
#                current_row += 1

            elif key == ord("q"):
                break

            self.menu(self.stdscr, current_row)
            self.stdscr.refresh()


print(pyfiglet.figlet_format("KitMan"))
time.sleep(2)
menu1 = Menu()
curses.wrapper(menu1.main)
