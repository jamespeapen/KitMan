'''
Data operations for Kitman
Read and write data to disk for persistent storage
Created 26 June 2020
Author: James Eapen
'''

from src.kitchen import Food, Recipie
import json


class Data:

    def read_pantry(self, filename):
        '''
        Read food objects from json file and make
        food objects from them
        :param filename: json file to read food objects from
        '''
        foods = {}
        with open(filename, 'r') as food_file:
            string = food_file.read()
            data = json.loads(string)
            for datum in data:
                food_obj = Food(**datum)
                foods[food_obj.name] = food_obj
        return foods

    def write_pantry(self, pantry, filename):
        '''
        write a list of foods to a json file
        :param foods: list of food objects
        :param filename: json file to write food objects to
        '''
        with open(filename, 'w') as file:

            foods = []
            for food in pantry:
                foods.append(pantry[food])

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

            file.write(json.dumps(
                [recipie.__dict__ for recipie in recipies], indent=4))

    def write_shopping_list(self, shopping_list, filename):
        '''
        writes shopping_list to file
        :param shopping_list: dict of foods and quantity needed
        :param filename: json file to write list to
        '''

        with open(filename, 'w') as shopping_list_writer:
            shopping_list_writer.write(json.dumps(shopping_list, indent=4))
        shopping_list_writer.close()
