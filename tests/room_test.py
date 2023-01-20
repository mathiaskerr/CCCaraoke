import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.guest = Guest("Mike", 30 , 50, "Fack")
        self.song_1 = Song("Respect", "Aretha Franlkin" , 2.30 )
        self.song_2 = Song("Fack", "Eminem" , 3.26 )
        self.song_3 = Song("Make it Wit Chu", "Queens of the Stone Age" , 3.59)

        song_list = [self.song_1, self.song_2, self.song_3]

        self.room = Room("Elvis Room", song_list, 20 , 2 )
    
    
    def test_room_has_name(self):
        self.assertEqual("Elvis Room", self.room.name)

    def test_room_cost(self):
        self.assertEqual(20, self.room.charge)

    def test_room_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_search_room_for_song_by_name(self):
        song = self.room.search_room_for_song("Respect")
        self.assertEqual("Respect", song.name)