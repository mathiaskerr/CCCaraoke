import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Mike", 30 , 50, "Fack")
        self.guest_2 = Guest("John",28, 99, "I Love Rock'n'Roll" )
        self.guest_list = [self.guest_1, self.guest_2]
        

        self.song_1 = Song("Respect", "Aretha Franlkin" , 2.30 )
        self.song_2 = Song("Fack", "Eminem" , 3.26 )
        self.song_3 = Song("Make it Wit Chu", "Queens of the Stone Age" , 3.59)

        song_list = [self.song_1, self.song_2, self.song_3]
        self.room = Room("Elvis Room", song_list, 20 , 2 )

    def test_guest_has_name(self):
        self.assertEqual("Mike", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest_1.wallet)

    def test_guest_has_age(self):
        self.assertEqual(30, self.guest_1.age)

    def test_guest_has_fav_song(self):
        self.assertEqual("Fack", self.guest_1.fav_song)

    def test_remove_from_wallet(self):
        self.guest_1.remove_from_wallet(self.room.charge)
        self.assertEqual(30, self.guest_1.wallet)