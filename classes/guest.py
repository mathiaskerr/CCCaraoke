class Guest:
    def __init__(self, name, age , wallet, fav_song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.fav_song = fav_song

    def remove_from_wallet(self, guests, purchased_item):
        paying_customer = guests[0]
        paying_customer.wallet -= purchased_item

        