"""
Kitchen defines the data structures used by Kitchen-Manager:
Food, Recipie, Grocery List, Pantry
@created: 2020 June 25
@author: James Eapen (jamespeapen@gmail.com)
"""


class Food:
    """
    The food class represents a food item with a
    name, a measuring unit and quantity needed
    """

    def __init__(self, name, category, unit, quantity_needed_in_stock=2):
        self._name = name
        self._category = category
        self._quantity_needed_in_stock = quantity_needed_in_stock
        self._unit = unit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """change the food name"""
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        """change the food category"""
        self._category = category

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unit):
        """change the food measuring unit"""
        self._unit = unit

    @property
    def quantity_needed_in_stock(self):
        return self._quantity_needed_in_stock

    @quantity_needed_in_stock.setter
    def quantity_needed_in_stock(self, quantity_needed_in_stock):
        """change the shopping priority"""
        self._quantity_needed_in_stock = quantity_needed_in_stock

class Recipie:
    """
    The recipie class represents a recipie with
    a dictionary of ingredients and their quatities,
    checks the pantry for necessary items and reports availability
    """

    def __init__(self, name, serving_number):
        self._name = name
        self._serving_number = serving_number
        self.ingredients = dict()

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

    def add_ingredient(self, ingredient, quantity_needed):
        if ingredient in self.ingredients:
            return "Ingredient already present"
        self.ingredients[ingredient] = quantity_needed

    def ingredient_quantity_needed(self, ingredient):
        return self.ingredients[ingredient]


    #TODO: check availability


class Kitchen:
    """
    The kitchen class represents the kitchen with
    a pantry and a recipie book
    """

    def __init__(self):
        self.recipies = list()  # list of recipies
        self.pantry = dict()  # dict of food and quantity
        self.shopping_list = list()  # list of food to buy

    @property
    def recipie_count(self):
        """get the number of recipies"""
        return len(self.recipies)

    def add_to_pantry(self, Food, quantity):
        if Food not in self.pantry:
            self.pantry[Food] = quantity
        else:
            self.pantry[Food] += quantity

    def add_recipie(self, recipie):
        self.recipies.append(recipie)

    def can_cook(self, recipie):
        for ingredient in recipie.ingredients:
            if self.pantry[ingredient] < recipie.ingredients[ingredient]:
                return False
        return True

    def get_cookable_recipies(self):
        cookable_recipies = []

        for recipie in self.recipies:
            if self.can_cook(recipie):
                cookable_recipies.append(recipie)
        return cookable_recipies

    def make_shopping_list(self):
        '''create a shopping list based on quantity_needed_in_stock'''
        self.shopping_list = []

        for food in self.pantry:
            if self.pantry[food] < food.quantity_needed_in_stock:
                self.shopping_list.append(food)
        return self.shopping_list

