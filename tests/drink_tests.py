import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Pint", 3)

    def test_drink_has_name(self):
        self.assertEqual("Pint", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink_1.price)    