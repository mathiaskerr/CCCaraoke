
class Room:
    def __init__(self, name, song_list, charge, capacity):
        self.name = name
        self.song_list = song_list
        self.charge = charge
        self.capacity = capacity
        self.people_in_room = []
        self.venue_till = 1000

    def search_room_for_song(self, song):
        for x in self.song_list:
            if x.name == song:
                return x

    def add_person_to_room(self, guest_list):
        for guest in guest_list:
            self.people_in_room.append(guest) 

    def checkout(self):
        self.people_in_room.clear()
