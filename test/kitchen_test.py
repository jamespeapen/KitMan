import sys
sys.path.append('../src')
from src.kitchen import Food, Recipie, Kitchen


class TestKitchen:
    '''Tests the kitchen module'''

    def test_food(self):

        # test init and independent parts
        food1 = Food(name='food01', unit='unit01', category='category01', quantity_needed_in_stock=5)
        assert food1.name == 'food01'
        assert food1.category == 'category01'
        assert food1.unit == 'unit01'
        assert food1.quantity_needed_in_stock == 5

        # test setters
        food1.name = 'food1'
        food1.category = 'category1'
        food1.unit = 'unit1'
        food1.quantity_needed_in_stock = 3
        food1.quantity = 5

        assert food1.name == 'food1'
        assert food1.category == 'category1'
        assert food1.unit == 'unit1'
        assert food1.quantity_needed_in_stock == 3

    def test_recipie(self):

        # test init and independent parts
        food2 = Food('food2', 'category2', 'unit2', quantity_needed_in_stock=5)
        recipie1 = Recipie('recipie01', serving_number=10)
        assert recipie1.name == 'recipie01'
        assert recipie1.serving_number == 10
        assert len(recipie1.ingredients) == 0

        # test setters
        recipie1.name = 'recipie1'
        recipie1.serving_number = 5
        recipie1.add_ingredient(food2, quantity_needed=10)

        assert recipie1.name == 'recipie1'
        assert recipie1.serving_number == 5
        assert len(recipie1.ingredients) == 1
        assert recipie1.ingredient_quantity_needed(food2) == 10

    def test_kitchen(self):

        # test init and independent parts
        kitchen1 = Kitchen()
        assert kitchen1.recipie_count == 0
        assert len(kitchen1.pantry) == 0

        # add food to pantry
        food3 = Food('food3', 'category3', 'unit3')     # default needed: 2, test needed 
        food4 = Food('food4', 'category4', 'unit4', quantity_needed_in_stock=4)     # test not needed 
        food5 = Food('food5', 'category5', 'unit5', quantity_needed_in_stock=10)    #test needed 

        kitchen1.add_to_pantry(food3, quantity=1)    # test needed 
        kitchen1.add_to_pantry(food4, quantity=7)    # test not needed 
        kitchen1.add_to_pantry(food5, quantity=4)    # test needed 
        assert len(kitchen1.pantry) == 3

        kitchen1.make_shopping_list()
        assert len(kitchen1.shopping_list) == 2    # food3, food5

        # add recipies
        recipie2 = Recipie('recipie2', serving_number=10)
        recipie2.add_ingredient(food3, quantity_needed=4)   # available: 2 - test can't cook
        kitchen1.add_recipie(recipie2)

        recipie3 = Recipie('recipie3', serving_number=1)
        recipie3.add_ingredient(food4, quantity_needed=4)   # available: 7 - test can cook
        kitchen1.add_recipie(recipie3)

        recipie4 = Recipie('recipie4', serving_number=3)
        recipie4.add_ingredient(food5, quantity_needed=5)   # available: 4 - test can't cook
        kitchen1.add_recipie(recipie4)

        assert kitchen1.can_cook(recipie3)
        assert not kitchen1.can_cook(recipie2)
        assert not kitchen1.can_cook(recipie4)

        assert len(kitchen1.get_cookable_recipies()) == 1     # recipie3
        assert kitchen1.get_cookable_recipies()[0].name == 'recipie3'

        # recipie with unavailable ingredient
        no_food = Food('nope', 'unavailable', 'none')
        recipie5 = Recipie('recipie5', serving_number=1)
        recipie5.add_ingredient(no_food, quantity_needed=3)

        assert not kitchen1.can_cook(recipie5)

