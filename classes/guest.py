class Guest:
    def __init__(self, name, age , wallet, fav_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song

    def remove_from_wallet(self, purchased_item):
        self.wallet -= purchased_item