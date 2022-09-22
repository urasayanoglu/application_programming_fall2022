from random import randint

class Coin:
    """A simple attempt to model a coin."""

    def __init__(self, sides=0):
        """Initialize coin side attribute."""
        self.sides = sides
        self.coin_sides = {0: "Tails", 1: "Heads"}

    def laying_position(self):
        """Telll the side of the coin before tossing."""
        print(f"{self.coin_sides[self.sides]} side of the coin is on top.")

    def toss_coin(self,toss_number=1):
        """Toss a coin."""
        for number in range(toss_number):
              print(self.coin_sides[randint(0, 1)])



bet1 = Coin()
bet1.laying_position()
bet2 = Coin()

bet1.toss_coin(10)
bet2.toss_coin(20)
bet1.toss_coin(50)


