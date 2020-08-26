from src.kitchen import Food, Recipie, Kitchen
import sys
sys.path.append('../src')


class TestKitchen:
    '''Tests the kitchen module'''

    def test_food(self):

        # test init and independent parts
        food1 = Food(name='food01',
                     unit='unit01',
                     category='category01',
                     quantity_needed_in_stock=5)

        assert food1.name == 'food01'
        assert food1.category == 'category01'
        assert food1.unit == 'unit01'
        assert food1.quantity_needed_in_stock == 5

        # test setters
        food1.name = 'food1'
        food1.category = 'category1'
        food1.unit = 'unit1'
        food1.quantity_needed_in_stock = 3

        assert food1.name == 'food1'
        assert food1.category == 'category1'
        assert food1.unit == 'unit1'
        assert food1.quantity_needed_in_stock == 3

    def test_recipie(self):

        food1 = Food('food1', 'category1', 'unit1', 1)
        food2 = Food('food2', 'category2', 'unit2', 2)
        food3 = Food('food3', 'category3', 'unit3', 3)

        recipie1 = Recipie('recipie1', 1, dict())
        recipie1.add_ingredient(food1, 11)
        recipie1.add_ingredient(food2, 12)

        recipie2 = Recipie('recipie2', 2, dict())
        recipie2.add_ingredient(food1, 21)
        recipie2.add_ingredient(food2, 22)
        recipie2.add_ingredient(food3, 23)

        assert recipie1.name == 'recipie1'
        assert recipie2.name == 'recipie2'

        assert recipie1.serving_number == 1
        assert recipie2.serving_number == 2

        assert len(recipie1.ingredients) == 2
        assert recipie1.ingredient_quantity_needed(food1) == 11
        assert recipie1.ingredient_quantity_needed(food2) == 12

        assert len(recipie2.ingredients) == 3
        assert recipie2.ingredient_quantity_needed(food1) == 21
        assert recipie2.ingredient_quantity_needed(food2) == 22
        assert recipie2.ingredient_quantity_needed(food3) == 23

        try:
            recipie1.add_ingredient(food1, 11)
        except RuntimeError:
            pass

    def test_kitchen(self):

        # test init and independent parts
        kitchen1 = Kitchen()
        assert kitchen1.recipie_count == 0
        assert len(kitchen1.pantry) == 0

        # add food to pantry
        # testing needed
        food1 = Food('food1',
                     'category1',
                     'unit1',
                     quantity_needed_in_stock=7)

        # test not needed
        food2 = Food('food2',
                     'category2',
                     'unit2',
                     quantity_needed_in_stock=4)

        # testing needed
        food3 = Food('food3',
                     'category3',
                     'unit3',
                     quantity_needed_in_stock=10)

        kitchen1.add_to_pantry(food1, quantity=6)    # testing needed
        kitchen1.add_to_pantry(food2, quantity=4)    # testing not needed
        kitchen1.add_to_pantry(food3, quantity=4)    # testing needed

        assert kitchen1.pantry[food1.name].quantity_in_stock == 6
        assert kitchen1.pantry[food2.name].quantity_in_stock == 4
        assert kitchen1.pantry[food3.name].quantity_in_stock == 4

        assert len(kitchen1.pantry) == 3

        kitchen1.make_shopping_list()
        assert len(kitchen1.shopping_list) == 2    # food1, food3
        assert kitchen1.shopping_list['food1'] == 1
        assert kitchen1.shopping_list['food3'] == 6

        # add recipies
        recipie1 = Recipie('recipie1', serving_number=10, ingredients=dict())

        # available: 1 - test can't cook
        recipie1.add_ingredient(food1, quantity_needed=9)

        # available: 7 - test can't cook
        recipie1.add_ingredient(food2, quantity_needed=9)

        kitchen1.add_recipie(recipie1)

        recipie2 = Recipie('recipie2', serving_number=1, ingredients=dict())

        # available: 7 - test can cook
        recipie2.add_ingredient(food2, quantity_needed=4)

        # available: 4 - test can cook
        recipie2.add_ingredient(food3, quantity_needed=4)

        kitchen1.add_recipie(recipie2)

        recipie3 = Recipie('recipie3', serving_number=3, ingredients=dict())

        # available: 4 - test can't cook
        recipie3.add_ingredient(food3, quantity_needed=6)

        kitchen1.add_recipie(recipie3)

        # duplicate recipie

        try:
            kitchen1.add_recipie(recipie3)
        except RuntimeError:
            pass

        # individual test
        assert kitchen1.can_cook(recipie2)
        assert not kitchen1.can_cook(recipie1)
        assert not kitchen1.can_cook(recipie3)

        # all cookable recipies
        assert len(kitchen1.get_cookable_recipies()) == 1     # recipie2
        assert kitchen1.get_cookable_recipies()[0].name == 'recipie2'

        # recipie with unavailable ingredient
        no_food = Food('nope', 'unavailable', 'none', 10)
        recipie4 = Recipie('recipie4', serving_number=1, ingredients=dict())
        recipie4.add_ingredient(no_food, quantity_needed=3)

        assert not kitchen1.can_cook(recipie4)

        # what_do_i_need_to_cook: unavailable ingredient
        food_needed = kitchen1.what_do_i_need_to_cook(recipie4)
        assert len(food_needed) == 1
        assert no_food in food_needed
        assert food_needed[no_food] == 3        # because we don't have it

        # what_do_i_need_to_cook: not enough ingredient
        food_needed = kitchen1.what_do_i_need_to_cook(recipie1)
        #assert len(food_needed) == 2
        assert food1 in food_needed
        assert food2 in food_needed
        assert food_needed[food1] == 3          # because we only have 1
        assert food_needed[food2] == 5          # because we only have 4
