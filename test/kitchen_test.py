import sys
sys.path.append('../src')
from src.kitchen import Food, Recipie, Kitchen


class TestKitchen:

    def test_food(self):

        #test initializaiton 
        food1 = Food('food1', 'grains', 'bags')
        assert food1.name == 'food1'
        assert food1._unit == 'bags'
        assert food1.quantity == 0
        assert food1.quantity_needed == 1

        #test need food function
        assert food1.need()

        #test setters 
        food1.name = 'food01'
        assert food1.name == 'food01'
        food1.quantity = 5
        assert not food1.need()

    def test_recipie(self):

        #test init
        recipie1 = Recipie('test', 5)
        assert recipie1.name == 'test'
        assert recipie1.serving_number == 5

        # test setters
        recipie1.name = 'recipie1'
        assert recipie1.name == 'recipie1'
        recipie1.serving_number = 10
        assert recipie1.serving_number == 10

        assert len(recipie1._ingredients) == 0

        # add ingredient
        recipie1.add_ingredient('ingredient1', 5)
        assert recipie1._ingredients['ingredient1'] == 5

        # duplciate ingredient
        assert recipie1.add_ingredient('ingredient1', 10) == 'Ingredient already present'
        assert recipie1._ingredients['ingredient1'] == 5

    def test_kitchen(self):

        # test init
        kitchen = Kitchen()
        assert  kitchen.recipie_count() == 0

