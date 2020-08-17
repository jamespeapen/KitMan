'''
Curses-based menu for the KitMan TUI
Created Aug 04 2020
Author: James Eapen (jamespeapen@gmail.com)
'''


import curses


class Menu:

    def __init__(self):

        self.stdscr = curses.initscr()

    def menu(self, stdscr, current_row):

        height, width = self.stdscr.getmaxyx()

        menu_bar = ["1: Kitchen", "2: Pantry", "3: Recipies", "4: Recipies", "5: Shopping"]

        y = 0
        x = 1

        for idx, element in enumerate(menu_bar):

            self.stdscr.addstr(y, x, element)
            x += len(element) + len(element) //5

        self.stdscr.refresh()

    def main(self, stdscr):

        curses.curs_set(0)

        current_row = 0

        self.menu(self.stdscr, current_row)

        while True:
            key = self.stdscr.getch()

            if (key == curses.KEY_UP or key == ord("k")) and current_row > 0:
                current_row -= 1

            elif (key == curses.KEY_DOWN or key == ord("j")) \
            and current_row < len(self.menu_list) - 1:
                current_row += 1

            elif key == ord("q"):
                break

            self.menu(self.stdscr, current_row)
            self.stdscr.refresh()


menu1 = Menu()
curses.wrapper(menu1.main)
