'''
Curses-based menu for the KitMan TUI
Created Aug 04 2020
Author: James Eapen (jamespeapen@gmail.com)
'''


import curses


class Menu:

    def __init__(self):

        self.stdscr = curses.initscr()
        self.menu_list = ["Kitchen", "Recipies", "Cook"]

    def menu(self, stdscr, current_row):

        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        height, width = self.stdscr.getmaxyx()

        for idx, element in enumerate(self.menu_list):

            y = height // 2 + idx
            x = width // 2 + len(element) // 2

            if idx == current_row:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, element)
                self.stdscr.attroff(curses.color_pair(1))

            else:
                self.stdscr.addstr(y, x, element)

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
