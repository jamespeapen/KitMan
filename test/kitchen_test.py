import sys
sys.path.append('../src')
from src.kitchen import Food


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





