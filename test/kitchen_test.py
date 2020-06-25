import sys
sys.path.append('../src')
from src.kitchen import Food, Recipie


class TestKitchen:

    def test_food(self):

        #test initializaiton 
        beans = Food('beans', 'grains', 'bags')
        assert beans.name == 'beans'
        assert beans._unit == 'bags'
        assert beans.quantity == 0
        assert beans.quantity_needed == 1
        assert beans.need()

        #test setters 
        beans.name = 'pinto'
        assert beans.name == 'pinto'
        beans.quantity = 5
        assert not beans.need()

    def test_recipie(self):

        #test init
        recipie1 = Recipie('test', 5)
        assert recipie1.name == 'test'
        assert recipie1.serving_number == 5

        recipie1.name = 'test2'
        assert recipie1.name == 'test2'
        recipie1.serving_number = 10
        assert recipie1.serving_number == 10

        assert len(recipie1._ingredients) == 0

        recipie1.add_ingredient('ingredient1', 5)
        assert recipie1._ingredients['ingredient1'] == 5

        assert recipie1.add_ingredient('ingredient1', 10) == 'Ingredient already present'
        assert recipie1._ingredients['ingredient1'] == 5




