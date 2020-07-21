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


    def read_food(self, filename):
        '''Read food objects from json file and make
        food objects from them'''
        foods = []
        with open(filename, 'r') as food_file:
            string = food_file.read()
            data = json.loads(string)
            for datum in data:
                food_obj = Food(**datum)
                foods.append(food_obj)
        return foods

    def write_food(self, foods, filename):
        '''write a list of foods to a json file'''
        with open(filename, 'w') as file:

            file.write(json.dumps([food.__dict__ for food in foods], indent=4))

    def read_recipies(self, filename):
        '''Read recipie objects from json file and make
        recipie objects from them'''
        recipies = []
        with open(filename, 'r') as recipie_file:
            string = recipie_file.read()
            data = json.loads(string)
            for datum in data:
                recipie_obj = Recipie(**datum)
                recipies.append(recipie_obj)
        return recipies


    def write_recipies(self, recipies, filename):
        '''write a list of recipies to json file'''
        with open(filename, 'w') as file:

            file.write(json.dumps([recipie.__dict__ for recipie in recipies], indent=4))

    def read_pantry(self, filename):
        pantry = {}
        with open(filename, 'r') as pantry_file:
            string = pantry_file.read()
            pantry_data = json.loads(string)
            for datum in pantry_data:
                pantry[datum['name']] = datum['quantity']
        return pantry

    def write_pantry(self):
        #TODO: write all pantry to file
        return True


    def write_shopping_list(self):
        #TODO: write shopping list to file
        return True
