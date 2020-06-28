'''
Data operations for Kitman
Read and write data to disk for persistent storage
Created 26 June 2020
Author: James Eapen
'''

from src.kitchen import Food, Recipie, Kitchen
from collections import namedtuple
import json

class Data:


    def __init__(self):
        self.writer
        self.reader

    def read_food_hook(self, food):
        return namedtuple('X', food.keys())(*food.values())

    def read_food(self, filename):
        foods = []
        with open(filename, 'r') as food_file:
            for line in food_file:
                food = json.loads(line)
                foods.append(food)
        return foods

    def write_food(self):
        #TODO: write all food objects to file
        return True


    def read_recipies(self):
        #TODO: read all recipies from file
        return True


    def write_recipies(self):
        #TODO: write all recipies to file
        return True


    def read_pantry(self):
        #TODO: read pantry contents to memory
        return True

    def write_pantry(self):
        #TODO: write all pantry to file
        return True


    def write_shopping_list(self):
        #TODO: write shopping list to file
        return True
