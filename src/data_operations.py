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
        '''
        Read food objects from json file and make
        food objects from them
        :param filename: json file to read food objects from 
        '''
        foods = []
        with open(filename, 'r') as food_file:
            string = food_file.read()
            data = json.loads(string)
            for datum in data:
                food_obj = Food(**datum)
                foods.append(food_obj)
        return foods

    def write_food(self, foods, filename):
        '''
        write a list of foods to a json file
        :param foods: list of food objects
        :param filename: json file to write food objects to 
        '''
        with open(filename, 'w') as file:

            file.write(json.dumps([food.__dict__ for food in foods], indent=4))

    def read_recipies(self, filename):
        '''
        Read recipie objects from json file and make
        recipie objects from them
        :param filename: json file to read recipie objects from
        '''
        recipies = []
        with open(filename, 'r') as recipie_file:
            string = recipie_file.read()
            data = json.loads(string)
            for datum in data:
                recipie_obj = Recipie(**datum)
                recipies.append(recipie_obj)
        return recipies


    def write_recipies(self, recipies, filename):
        '''
        write a list of recipies to json file
        :param recipies: list of recipie objects
        :param filename: json file to write recipies to
        '''

        with open(filename, 'w') as file:

            file.write(json.dumps([recipie.__dict__ for recipie in recipies], indent=4))

    def read_pantry(self, filename):
        '''
        reads pantry contents from file. only the names and quantity
        are written to disk
        @recipies: list of recipie objects
        :param filename: the json file containing pantry data
        '''


        with open(filename, 'r') as pantry_file_reader:
            pantry = json.loads(pantry_file_reader.read())
        return pantry

    def write_pantry(self, pantry, filename):
        '''
        writes the names and quantity of food objects in the pantry to file
        :param pantry: dictionary of foods and their quantities from a Kitchen object
        :param filename: json file to write pantry to
        '''

        writable_pantry = {}

        # extract names and quantities
        for food in pantry:
            writable_pantry[food.name] = pantry[food]

        with open(filename, 'w') as pantry_file_writer:
            pantry_file_writer.write(json.dumps(writable_pantry, indent=4))
        pantry_file_writer.close()

    def write_shopping_list(self):
        #TODO: write shopping list to file
        return True
