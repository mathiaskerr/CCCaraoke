
class Room:
    def __init__(self, name, song_list, charge, capacity):
        self.name = name
        self.song_list = song_list
        self.charge = charge
        self.capacity = capacity
        self.people_in_room = []
        self.venue_till = 1000
        self.bar_tab = 0

    def search_room_for_song(self, song):
        for x in self.song_list:
            if x.name == song:
                return x

    def add_person_to_room(self, guest_list):
        if self.capacity - len(self.people_in_room) >= len(guest_list):
            for guest in guest_list:
                self.people_in_room.append(guest) 
        else:
            return "This room does not have enough space"        

    def checkout(self):
        self.people_in_room.clear()

    def add_to_till(self, purchased_item):
        self.venue_till += purchased_item    

    def check_in_and_pay(self, guests, room_cost):
        paying_customer = guests[0]
        self.add_person_to_room(guests)
        self.add_to_till(room_cost)
        paying_customer.remove_from_wallet(room_cost)

    def favourite_song(self, song):
        for x in self.song_list:
            if x.name == song:
                return "Whoooo"

    def add_to_bar_tab(self, purchased_item):
        self.bar_tab += purchased_item

    def pay_bar_tab(self , guests,  bar_tab):
        paying_customer = guests[0]
        paying_customer.remove_from_wallet(bar_tab)
        self.add_to_till(bar_tab)
        self.bar_tab -= self.bar_tab
        
                