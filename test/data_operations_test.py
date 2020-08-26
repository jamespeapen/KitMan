from src.kitchen import Food, Recipie, Kitchen
from src.data_operations import Data
import json

class TestData:
    '''Tests the data module'''


    def test_write_pantry(self):

        # initialize kitchen with food and recipies
        kitchen = Kitchen()

        food1 = Food(name='food1', unit='unit1', category='category1', quantity_needed_in_stock=10)
        food2 = Food('food2', 'category2', 'unit2', quantity_needed_in_stock=20)

        kitchen.add_to_pantry(food1, 10)
        kitchen.add_to_pantry(food2, 20)

        data = Data()
        data.write_pantry(kitchen.pantry, 'test/test_write_pantry.json')

        # check file for valid json objects
        with open('test/test_write_pantry.json') as file:
            json_data = json.loads(file.read())

            assert type(json_data[0]) == dict
            assert json_data[0]['_name'] == 'food1'
            assert json_data[0]['_unit'] == 'unit1'
            assert json_data[0]['_category'] == 'category1'
            assert json_data[0]['_quantity_needed_in_stock'] == 10
            assert json_data[0]['_quantity_in_stock'] == 10

            assert type(json_data[1]) == dict
            assert json_data[1]['_name'] == 'food2'
            assert json_data[1]['_unit'] == 'unit2'
            assert json_data[1]['_category'] == 'category2'
            assert json_data[1]['_quantity_needed_in_stock'] == 20
            assert json_data[1]['_quantity_in_stock'] == 20

        file.close()

        # clear file after test
        #with open('test/test_write_pantry.json', 'w') as file:
              #file.write('')

    def test_read_pantry(self):
        data = Data()
        foods = data.read_pantry('test/test_read_food.json')

        assert len(foods) == 2

        # check that Food objects are the value in the pair
        for food in foods:
            assert isinstance(foods[food], Food)

        # check object attributes
        assert foods['food4'].name == 'food4'
        assert foods['food4'].unit == 'unit4'
        assert foods['food4'].category == 'category4'
        assert foods['food4'].quantity_needed_in_stock == 4

        assert foods['food5'].name == 'food5'
        assert foods['food5'].unit == 'unit5'
        assert foods['food5'].category == 'category5'
        assert foods['food5'].quantity_needed_in_stock == 5

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

    def test_write_recipies(self):
        data = Data()

        recipie1 = Recipie('recipie01', 10, dict())
        recipie2 = Recipie('recipie02', 20, {'ingredient21': 21, 'ingredient22': 22})
        recipie3 = Recipie('recipie03', 30, {'ingredient31': 31, 'ingredient32': 32, 'ingredient33': 33})
        recipies = [recipie1, recipie2, recipie3]

        data.write_recipies(recipies, 'test/test_write_recipies.json')
        with open('test/test_write_recipies.json', 'r') as file:
            json_data = json.loads(file.read())
            assert type(json_data[0]) == dict
            assert type(json_data[1]) == dict
            assert type(json_data[2]) == dict

            assert json_data[0]['_name'] == 'recipie01'
            assert json_data[1]['_name'] == 'recipie02'
            assert json_data[2]['_name'] == 'recipie03'

            assert json_data[0]['_serving_number'] == 10
            assert json_data[1]['_serving_number'] == 20
            assert json_data[2]['_serving_number'] == 30

            assert type(json_data[0]['ingredients']) == dict
            assert type(json_data[1]['ingredients']) == dict
            assert type(json_data[2]['ingredients']) == dict

            assert len(json_data[0]['ingredients']) == 0
            assert len(json_data[1]['ingredients']) == 2
            assert len(json_data[2]['ingredients']) == 3

            assert json_data[1]['ingredients']['ingredient21'] == 21
            assert json_data[1]['ingredients']['ingredient22'] == 22
            assert json_data[2]['ingredients']['ingredient31'] == 31
            assert json_data[2]['ingredients']['ingredient32'] == 32
            assert json_data[2]['ingredients']['ingredient33'] == 33

        file.close()

        # clear file after test
        with open('test/test_write_recipies.json', 'w') as file:
              file.write('')
        file.close()

    def test_write_shopping_list(sefl):

        kitchen1 = Kitchen()
        assert len(kitchen1.pantry) == 0

        # add food to pantry
        food1 = Food('food1', 'category1', 'unit1', quantity_needed_in_stock=2)
        food2 = Food('food2', 'category2', 'unit2', quantity_needed_in_stock=4)
        food3 = Food('food3', 'category3', 'unit3', quantity_needed_in_stock=10)

        kitchen1.add_to_pantry(food1, quantity=1)    # in list
        kitchen1.add_to_pantry(food2, quantity=7)    # not in list
        kitchen1.add_to_pantry(food3, quantity=4)    # in list

        assert len(kitchen1.pantry) == 3

        kitchen1.make_shopping_list()
        assert len(kitchen1.shopping_list) == 2

        data = Data()
        data.write_shopping_list(kitchen1.shopping_list, 'test/test_write_shopping_list.json')

        with open('test/test_write_shopping_list.json', 'r') as list_reader:
            written_list = json.loads(list_reader.read())
            assert written_list['food1'] == 1
            assert written_list['food3'] == 6
        list_reader.close()
