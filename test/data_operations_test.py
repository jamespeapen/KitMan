from src.kitchen import Food, Recipie, Kitchen
from src.data_operations import Data
import json

class TestData:
    '''Tests the data module'''


    def test_write_food(self):

        # initialize kitchen with food and recipies
        kitchen = Kitchen()

        food1 = Food(name='food1', unit='unit1', category='category1', quantity_needed_in_stock=10)
        food2 = Food('food2', 'category2', 'unit2', quantity_needed_in_stock=20)
        foods = [food1, food2]

        kitchen.add_to_pantry(food1, 10)
        kitchen.add_to_pantry(food2, 20)

        recipie1 = Recipie('recipie01', serving_number=10)
        recipie2 = Recipie('recipie02', serving_number=20)

        kitchen.add_recipie(recipie1)
        kitchen.add_recipie(recipie2)


        data = Data()
        data.write_food(foods, 'test/test_write_food.json')

        # check file for valid json objects
        with open('test/test_write_food.json') as file:
            line = file.read()
            json_data = json.loads(line)
            assert type(json_data[0]) == dict
            assert type(json_data[1]) == dict
            assert json_data[0]['_name'] == 'food1'
            assert json_data[0]['_unit'] == 'unit1'
            assert json_data[0]['_category'] == 'category1'
            assert json_data[0]['_quantity_needed_in_stock'] == 10
            assert json_data[1]['_name'] == 'food2'
            assert json_data[1]['_unit'] == 'unit2'
            assert json_data[1]['_category'] == 'category2'
            assert json_data[1]['_quantity_needed_in_stock'] == 20
        file.close()

        # clear file after test
        with open('test/test_write_food.json', 'w') as file:
              file.write('')

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

    def test_read_recipies(self):
        data = Data()
        recipies = data.read_recipies('test/test_read_recipies.json')

        assert len(recipies) == 2

        for recipie in recipies:
            assert isinstance(recipie, Recipie)

        test_recipie1 = recipies[0]
        assert test_recipie1.name == 'test_recipie1'
        assert test_recipie1.serving_number == 1
        assert isinstance(test_recipie1.ingredients, dict)
        assert test_recipie1.ingredients['ingredient11'] == 11
        assert test_recipie1.ingredients['ingredient12'] == 12

        test_recipie2 = recipies[1]
        assert test_recipie2.name == 'test_recipie2'
        assert test_recipie2.serving_number == 2
        assert isinstance(test_recipie2.ingredients, dict)
        assert test_recipie2.ingredients['ingredient21'] == 21
        assert test_recipie2.ingredients['ingredient22'] == 22
