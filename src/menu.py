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

        # kitchen and data objects
        self.data = Data()
        self.kitchen = Kitchen()
        self.foods = self.data.read_food('test/test_read_food.json')
        self.kitchen.pantry = self.data.read_pantry('test/test_read_pantry.json')
        self.kitchen.recipies = self.data.read_recipies('test/test_read_recipies.json')

        # main screen
        self.stdscr = curses.initscr()
        self.height, self.width = self.stdscr.getmaxyx()

        # windows
        self.menubar = curses.newwin(2, self.width, 0, 0)

        self.data_window = curses.newwin(self.height - 3,
                                         (self.width // 2), 3, 0)

        self.preview_window = curses.newwin(self.height - 3,
                                            self.width // 2, 3,
                                            (self.width // 2))

        # colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def menu(self, stdscr, current_row):
        """Main menu bar"""

        menu_bar = ["1: Pantry",
                    "2: Recipies",
                    "3: Shopping"]

        y = 0
        x = 1

        for idx, element in enumerate(menu_bar):

            self.menubar.addstr(y, x, element)
            x += len(element) + len(menu_bar) // (len(menu_bar) - 1)

        self.menubar.refresh()

    def pantry(self, stdscr, current_row):
        """Show pantry in the data window and food details
        in the preview window"""

        self.data_window.clear()
        self.preview_window.clear()

        self.data_window.addstr(0, 0, "Food\tQuantity in stock")
        y = 2
        x = 0

        for idx, food in enumerate(self.kitchen.pantry):
            if idx == current_row:
                self.data_window.attron(curses.color_pair(1))
                self.data_window.addstr(y, x, food + '\t' + str(self.kitchen.pantry[food]))
                self.data_window.attroff(curses.color_pair(1))
                self.preview_window.addstr(str(self.kitchen.pantry[food]))
            else:
                self.data_window.addstr(y, x, food + '\t' + str(self.kitchen.pantry[food]))

            y += 2

        self.data_window.refresh()
        self.preview_window.refresh()

    def recipies(self, stdscr, current_row):
        """show recipies in the data window and details
        in preview window"""

        self.data_window.clear()
        self.preview_window.clear()

        self.data_window.addstr(0, 0, "Recipies")
        self.preview_window.addstr(0, 0, "Ingredient\tQuantity\n\n")
        y = 2
        x = 0

        for idx, recipie in enumerate(self.kitchen.recipies):
            if idx == current_row:
                self.data_window.attron(curses.color_pair(1))
                self.data_window.addstr(y, x, recipie.name)
                self.data_window.attroff(curses.color_pair(1))
                for ingredient in recipie.ingredients:
                    self.preview_window.addstr(ingredient + '\t' + str(recipie.ingredients[ingredient]) + '\n\n')

            else:
                self.data_window.addstr(y, x, recipie.name)

            y += 2

        self.data_window.refresh()
        self.preview_window.refresh()

    def refresh_data_window(self, stdscr, current_row, menu_mode):
        """Check what menu item method was selected before scroll event
        and call that method"""

        if menu_mode == 1:
            self.pantry(stdscr, current_row)
        elif menu_mode == 2:
            self.recipies(stdscr, current_row)

    def main(self, stdscr):
        """Main event loop and scroll control"""

        curses.curs_set(0)

        current_row = 0

        self.menu(self.stdscr, current_row)

        while True:
            key = self.stdscr.getch()

            # main menu selection
            if key == ord('1'):
                current_row = 0
                self.pantry(stdscr, current_row)
                menu_mode = 1

            elif key == ord('2'):
                current_row = 0
                self.recipies(stdscr, current_row)
                menu_mode = 2

            elif key == ord("q"):
                break

            # scrolling
            elif (key == curses.KEY_UP or key == ord("k")) \
            and current_row > 0:
                current_row -= 1
                self.refresh_data_window(stdscr, current_row, menu_mode)

            elif (key == curses.KEY_DOWN or key == ord("j")):

                if menu_mode == 1 \
                and current_row < len(self.kitchen.pantry) - 1:
                    current_row += 1

                if menu_mode == 2 \
                and current_row < len(self.kitchen.recipies) - 1:
                    current_row += 1

                self.refresh_data_window(stdscr, current_row, menu_mode)
            self.stdscr.refresh()


print(pyfiglet.figlet_format("KitMan"))
time.sleep(0.2)
menu1 = Menu()
curses.wrapper(menu1.main)
