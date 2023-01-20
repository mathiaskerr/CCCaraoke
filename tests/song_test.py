import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):

        self.song_1 = Song("Respect", "Aretha Franlkin" , 2.30 )

    def test_song_has_name(self):
        self.assertEqual("Respect", self.song_1.name)

    def test_guest_has_artist(self):
        self.assertEqual("Aretha Franlkin", self.song_1.artist)

    def test_guest_has_length(self):
        self.assertEqual(2.30, self.song_1.length)