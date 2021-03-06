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
        self.kitchen.pantry = self.data.read_pantry('src/demo/pantry.json')
        self.kitchen.recipies = self.data.read_recipies('src/demo/recipies.json')

        # main screen
        self.stdscr = curses.initscr()
        self.height, self.width = self.stdscr.getmaxyx()

        # windows
        self.menubar = curses.newwin(2, self.width, 0, 0)
        self.menubar.addstr("Kitman")
        self.menubar.refresh()

        self.data_window = curses.newwin(self.height - 5,
                                         (self.width // 2), 3, 0)

        self.preview_window = curses.newwin(self.height - 5,
                                            self.width // 2, 3,
                                            (self.width // 2))

        self.option_window = curses.newwin(2, self.width, self.height-2, 0)

        # colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def menu(self, stdscr, current_row, menu_mode):
        """Main menu bar"""

        menu_bar = ["1: Pantry ",
                    "2: Recipies ",
                    "3: Shopping "]

        y = 0
        x = 1

        for idx, element in enumerate(menu_bar):

            if idx == menu_mode - 1:
                self.menubar.attron(curses.color_pair(1))
                self.menubar.addstr(y, x, element)
                self.menubar.attroff(curses.color_pair(1))
            else:
                self.menubar.addstr(y, x, element)

            # word spacing
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

            food_obj = self.kitchen.pantry[food]

            # highlight current row
            if idx == current_row:
                self.data_window.attron(curses.color_pair(1))
                self.data_window.addstr(y, x, food.capitalize() + '\t' + str(food_obj.quantity_in_stock) + ' ' + food_obj.unit)
                self.data_window.attroff(curses.color_pair(1))
                self.preview_window.addstr(str(food_obj))
            else:
                self.data_window.addstr(y, x, food.capitalize() + '\t' + str(food_obj.quantity_in_stock) + ' ' + food_obj.unit)

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
        x = 1

        for idx, recipie in enumerate(self.kitchen.recipies):
            if idx == current_row:
                self.data_window.attron(curses.color_pair(1))
                self.data_window.addstr(y, x, recipie.name.capitalize())
                self.data_window.attroff(curses.color_pair(1))
                for ingredient in recipie.ingredients:
                    self.preview_window.addstr(ingredient.capitalize() + '\t'
                                               + str(recipie.ingredients[ingredient]) + ' '
                                               + self.kitchen.pantry[ingredient].unit + '\n\n')
                for instruction in recipie.instructions:
                    self.preview_window.addstr(instruction.capitalize() + '\n\n')

            else:
                self.data_window.addstr(y, x, recipie.name.capitalize())

            y += 2

        self.data_window.refresh()
        self.preview_window.refresh()

    def options(self, stdscr, current_row, menu_mode):
        """Options for additions, removals, modifications etc."""

        self.option_window.clear()

        pantry_options = ["a: Add to stock", "r: Remove from stock", "c: Change stock", "m: Modify food"]
        recipie_options = ["a: Add", "r: Remove", "m: Modify"]

        if menu_mode == 1:
            for element in pantry_options:
                self.option_window.addstr(element + "\t")
        elif menu_mode == 2:
            for element in recipie_options:
                self.option_window.addstr(element + "\t")

        self.option_window.refresh()

    def refresh_data_window(self, stdscr, current_row, menu_mode):
        """Check what menu item method was selected with scroll event
        and call that method"""

        if menu_mode == 1:
            self.pantry(stdscr, current_row)
        elif menu_mode == 2:
            self.recipies(stdscr, current_row)

        self.menu(stdscr, current_row, menu_mode)
        self.options(stdscr, current_row, menu_mode)

    def main(self, stdscr):
        """Main event loop and scroll control"""

        curses.curs_set(0)

        menu_mode = 1
        current_row = 0

        self.menu(self.stdscr, current_row, 1)
        self.options(stdscr, current_row, 1)
        self.pantry(stdscr, current_row)

        while True:
            key = self.stdscr.getch()

            # main menu selection
            if key == ord('1') or key == ord('h') and menu_mode == 2:
                current_row = 0
                menu_mode = 1
                self.refresh_data_window(stdscr, current_row, menu_mode)

            elif key == ord('2') \
                or key == ord('l') and menu_mode == 1 \
                or key == ord('h') and menu_mode == 3:
                menu_mode = 2
                current_row = 0
                self.refresh_data_window(stdscr, current_row, menu_mode)

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

                elif menu_mode == 2 \
                and current_row < len(self.kitchen.recipies) - 1:
                    current_row += 1

                self.refresh_data_window(stdscr, current_row, menu_mode)
            self.stdscr.refresh()


print(pyfiglet.figlet_format("KitMan"))
time.sleep(0.2)
menu1 = Menu()
curses.wrapper(menu1.main)
