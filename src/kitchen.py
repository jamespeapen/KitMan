"""
Kitchen defines the data structures used by Kitchen-Manager:
Food, Recipie, Grocery List, Pantry
@created: 2020 June 25
@author: James Eapen (jamespeapen@gmail.com)
"""


class Food:
    """
    The food class represents a food item with a
    name, quatity, and shopping priority
    """

    def __init__(self, name, category, unit, quantity=0, quantity_needed=1):
        self._name = name
        self._category = category
        self._quantity = quantity
        self._quantity_needed = quantity_needed
        self._unit = unit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """change the food name"""
        self._name = name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """change the quantity of food available"""
        self._quantity = quantity

    @property
    def quantity_needed(self):
        return self._quantity_needed

    @quantity_needed.setter
    def quantity_needed(self, quantity_needed):
        """change the shopping priority"""
        self._quantity_needed = quantity_needed

    def need(self):
        return self._quantity < self._quantity_needed


class Recipie:
    """
    The recipie class represents a recipie with
    a dictionary of ingredients and their quatities,
    checks the pantry for necessary items and reports availability
    """

    def __init__(self, name, serving_number):
        self._name = name
        self._serving_number = serving_number
        self._ingredients = dict()

    @property
    def name(self):
        """get the recipie name"""
        return self._name

    @name.setter
    def name(self, name):
        """change the recipie name"""
        self._name = name

    @property
    def serving_number(self):
        return self._serving_number

    @serving_number.setter
    def serving_number(self, number):
        self._serving_number = number

    def add_ingredient(self, ingredient, quantity):
        if ingredient in self._ingredients:
            return "Ingredient already present"
        self._ingredients[ingredient] = quantity

    #TODO: check availability


class Kitchen:
    """
    The kitchen class represents the kitchen with
    a pantry and a recipie book
    """

    def __init__(self):
        self._recipies = list()  # list of recipies
        self._pantry = dict()  # dict of food and quantity
        self._shopping_list = list()  # list of food to buy

    @property
    def recipie_count(self):
        """get the number of recipies"""
        return len(self._recipies)
