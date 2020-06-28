from src.kitchen import Food, Recipie, Kitchen
from src.data_operations import Data
import json

class TestData:
    '''Tests the data module'''

    # initialize kitchen with food and recipies
    kitchen = Kitchen()

    food1 = Food(name='food1', unit='unit1', category='category1', quantity_needed_in_stock=1)
    food2 = Food('food2', 'category2', 'unit2', quantity_needed_in_stock=1)

    kitchen.add_to_pantry(food1, 10)
    kitchen.add_to_pantry(food2, 20)

    recipie1 = Recipie('recipie01', serving_number=10)
    recipie2 = Recipie('recipie02', serving_number=20)

    kitchen.add_recipie(recipie1)
    kitchen.add_recipie(recipie2)

    def test_read_food(self):
        data = Data()
        foods = data.read_food('test/test_read_food.json')

        assert len(foods) == 2

        # check that Food objects are returned
        for food in foods:
            assert isinstance(food, Food)

        # check object attributes
        assert foods[0].name == 'food4'
        assert foods[0].unit == 'unit4'
        assert foods[0].category == 'category4'
        assert foods[0].quantity_needed_in_stock == 4

        assert foods[1].name == 'food5'
        assert foods[1].unit == 'unit5'
        assert foods[1].category == 'category5'
        assert foods[1].quantity_needed_in_stock == 5
