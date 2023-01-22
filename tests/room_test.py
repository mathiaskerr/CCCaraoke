import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.guest_1 = Guest("Mike", 30 , 50, "Fack")
        self.guest_2 = Guest("John",28, 99, "I Love Rock'n'Roll" )
        self.guest_list = [self.guest_1, self.guest_2]

        self.song_1 = Song("Respect", "Aretha Franlkin" , 2.30 )
        self.song_2 = Song("Fack", "Eminem" , 3.26 )
        self.song_3 = Song("Make it Wit Chu", "Queens of the Stone Age" , 3.59)

        song_list = [self.song_1, self.song_2, self.song_3]

        self.room = Room("Elvis Room", song_list, 20 , 2 )

        self.drink_1 = Drink("Pint", 3)
        self.drink_2 = Drink("Cocktail", 10)
        self.drink_3 = Drink("Wine", 4)

    
    
    def test_room_has_name(self):
        self.assertEqual("Elvis Room", self.room.name)

    def test_room_cost(self):
        self.assertEqual(20, self.room.charge)

    def test_room_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_search_room_for_song_by_name(self):
        song = self.room.search_room_for_song("Fack")
        self.assertEqual("Fack", song.name)

    def test_add_person_to_room(self):
        guest_list = [self.guest_1]
        self.room.add_person_to_room(guest_list)
        self.assertEqual(1, len(self.room.people_in_room))

    def test_add_multiple_persons_to_room(self):
        self.room.add_person_to_room(self.guest_list)
        self.assertEqual(2, len(self.room.people_in_room))

    def test_checkout_from_room(self):
        self.room.add_person_to_room(self.guest_list)
        self.room.checkout()
        self.assertEqual(0,len(self.room.people_in_room))
        
    def test_add_money_to_till(self):
        self.room.add_to_till(self.room.charge)
        self.assertEqual(1020, self.room.venue_till)

    def test_check_in_and_pay(self):
        self.room.check_in_and_pay(self.guest_list , self.room.charge)
        self.assertEqual(2, len(self.room.people_in_room))
        self.assertEqual(1020, self.room.venue_till)
        self.assertEqual(30, self.guest_1.wallet)

    def test_favourite_song(self):
        # self.room.search_room_for_song(self.guest_1.fav_song)
        self.assertEqual("Whoooo", self.room.favourite_song(self.guest_1.fav_song))

    def test_add_drink_to_bar_tab(self):
        self.room.add_to_bar_tab(self.drink_1.price)
        self.room.add_to_bar_tab(self.drink_2.price)
        self.assertEqual(13, self.room.bar_tab)

    def test_pay_bar_tab(self):
        self.room.add_to_bar_tab(self.drink_1.price)
        self.room.add_to_bar_tab(self.drink_2.price)
        self.room.pay_bar_tab(self.guest_list, self.room.bar_tab)
        self.assertEqual(37, self.guest_1.wallet)
        self.assertEqual(1013, self.room.venue_till)
        self.assertEqual(0 , self.room.bar_tab)