'''
War_Game
'''

# Card Class(Single card class)

import random

# Golbal Variables:
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank +' of '+ self.suit


# Actual cards are 52,
# Hence there is the deck of cards

# Create Deck Class(Holds 52 cards)
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Player need to be named and they can hold
# one or more than one cards
# Remove one card from the top of the deck
# By making list[0] is top od deck and
# list[-1] as bottom of deck

# Create Player Class

class Player:
    def __init__(self,name):
        self.name = name
        # Player get cards
        self.all_cards = []

    def add_cards(self,new_card):

        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def remove_one(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'The Player {self.name} has {len(self.all_cards)} cards'

# Setup the Players
player_one = Player('One')
player_two = Player('Two')


# Setup the Deck of cards
cards_deck = Deck()


# Shuffle the Deck of cards
cards_deck.shuffle()

# Split equal shares of cards for two playes
for x in range(len(cards_deck.all_cards)//2):
    player_one.add_cards(cards_deck.deal_one())
    player_two.add_cards(cards_deck.deal_one())


# Main Code
game_on = True
round_count = 0

while game_on:
    round_count += 1
    print(f"Round {round_count}")

    # Check Players holds cards or not
    if len(player_one.all_cards) == 0:
        print("Player One is Out Cards")
        print("Player Two wins")
        game_on = False
        break

    elif len(player_two.all_cards) == 0:
        print("Player Two is Out Cards")
        print("Player One wins")
        game_on = False
        break

    else:
        # Put Cut On the table from hand
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        
        at_war = True

        while at_war:
            # Compare two cards by values
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
                break

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
                break

            else:
                # Two cards are equal
                print("War")

                # The player One has less number of cards
                if len(player_one.all_cards) < 6:
                    print("Player One has less number Cards")
                    print("Player Two wins")
                    game_on = False
                    break
                # The player Two has less number of cards
                elif len(player_two.all_cards) < 6:
                    print("Player Two has less number Cards")
                    print("Player One wins")
                    game_on = False
                    break

                else:
                    # Pass Six Cards by both players
                    for i in range(6):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())