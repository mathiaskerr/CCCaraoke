import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mike", 30 , 50, "Fack")

    def test_guest_has_name(self):
        self.assertEqual("Mike", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_age(self):
        self.assertEqual(30, self.guest.age)

    def test_guest_has_fav_song(self):
        self.assertEqual("Fack", self.guest.fav_song)
