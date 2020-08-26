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

    def __init__(self, name, category, unit, quantity_needed_in_stock, quantity_in_stock=0, *args, **kwargs):
        self._name = name
        self._category = category
        self._unit = unit
        self._quantity_needed_in_stock = quantity_needed_in_stock
        self._quantity_in_stock=quantity_in_stock

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

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity_in_stock):
        """change the current stock amount"""
        self._quantity_in_stock = quantity_in_stock


class Recipie:
    """
    The recipie class represents a recipie with
    a dictionary of ingredients and their quantities,
    checks the pantry for necessary items and reports availability
    BUG: when a recipie is initialized without a populated dictionary,
    it needs the ingredient=dict() specified. Without it, the last recipie
    object's ingredient dictionary becomes
    the new objects ingredient dictionary
    """

    def __init__(self,
                 name,
                 serving_number,
                 ingredients=dict(),
                 *args,
                 **kwargs):
        self._name = name
        self._serving_number = serving_number
        # self.ingredients = dict() # last version without json reading support

        # when reading from json, the ingredient dictionary may be
        # populated, when just creating a recipie, it can be empty
        self.ingredients = ingredients

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
            raise RuntimeError("Ingredient already present")
        self.ingredients[ingredient] = quantity_needed

    def ingredient_quantity_needed(self, ingredient):
        return self.ingredients[ingredient]


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

    def add_to_pantry(self, food, quantity):
        """add food to pantry if not already in"""
        if food.name not in self.pantry:
            self.pantry[food.name] = food
            self.pantry[food.name].quantity_in_stock = quantity
        else:
            self.pantry[food.name].quantity_in_stock += quantity

    def add_recipie(self, recipie):
        """add recipie to pantry"""
        for each_recipie in self.recipies:
            if recipie.name == each_recipie.name:
                raise RuntimeError('Recipie already present')
        self.recipies.append(recipie)

    def what_do_i_need_to_cook(self, recipie):
        food_needed = {}

        for ingredient in recipie.ingredients:
            if ingredient.name not in self.pantry:
                food_needed[ingredient] = recipie.ingredients[ingredient]

            elif recipie.ingredients[ingredient] > self.pantry[ingredient.name].quantity_in_stock:
                food_needed[ingredient] = recipie.ingredients[ingredient] \
                - self.pantry[ingredient.name].quantity_in_stock

        return food_needed

    def can_cook(self, recipie):
        """check if the ingredients for the recipie are in the pantry
        in the required quantities"""
        for ingredient in recipie.ingredients:
            if ingredient.name not in self.pantry:
                return False
            elif self.pantry[ingredient.name].quantity_in_stock < recipie.ingredients[ingredient]:
                return False
        return True

    def get_cookable_recipies(self):
        """get all recipies for which ingredients are present in
        required quantities in the panty"""
        cookable_recipies = []

        for recipie in self.recipies:
            if self.can_cook(recipie):
                cookable_recipies.append(recipie)
        return cookable_recipies

    def make_shopping_list(self):
        '''create a shopping list based on quantity_needed_in_stock and
        current quantities'''
        self.shopping_list = {}

        for food_name in self.pantry:
            if self.pantry[food_name].quantity_in_stock < self.pantry[food_name].quantity_needed_in_stock:
                self.shopping_list[food_name] = self.pantry[food_name].quantity_needed_in_stock \
                    - self.pantry[food_name].quantity_in_stock

        return self.shopping_list
