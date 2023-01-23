#cash game

import random
import itertools
import time

class Deck:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def fill(self):
        for suits, values in itertools.product(suits, values):
            self.cards.append(Card(suits, values))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def clear(self):
        for x in range(len(self.cards)):
            self.cards.pop(x)


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def getValue(self):
        try:
            val = 4*int(self.value)
        except ValueError:
            if self.value == "Jack":
                val = 44
            elif self.value == "Queen":
                val = 48
            elif self.value == "King":
                val = 52
            elif self.value == "Ace":
                val = 56
            else: print("Error")
        if self.suit == "Hearts":
            val += 1
        elif self.suit == "Spades":
            val += 2
        elif self.suit == "Clubs":
            val += 3
        else: print("Error")
        return val

    def print_name(self):
        return f"{self.value} of {self.suit}"


class Player:
    def __init__(self):
        self.card = []
       
    def receive_card(self, card):
        self.card.append(card)

    def get_card_score(self):
        return self.card[0].getValue()
 

class Human(Player):
    def __init__(self, tokens):
        super().__init__(self)
        self.tokens = tokens

    def bet(self):
        try:
            amt = int(input("How much would you like to bet? You have", self.tokens, "tokens"))
            if amt > self.tokens:
                print("You don't have that many tokens, please try again")
                self.bet()
            else:
                self.tokens -= amt
                print("Betting", amt, "tokens. You have ", self.tokens, "tokens left")
                return amt
        except ValueError:
            print("That is not a valid bet entry, please try again.")
            self.bet()
         

class Board:
    def __init__(self, tokens):
        self.tokens = tokens

    def print_board(self):
        print("There are", self.tokens, "tokens on the board")

    def add_tokens(self, amt):
        self.tokens += (2*amt)

    def cash_out(self):
        amt = self.tokens
        self.tokens = 0
        return amt


class Game:

    num_players = 1
    num_tokens = 100

    def __init__(self, num_tokens):
        self.deck1 = Deck()
        self.table = Board(0)
        self.player1 = Human([], num_tokens)
        self.dealer1 = Player([])

    def deal(self):
        self.player1.receive_card(self.deck1.deal())
        self.dealer1.receive_card(self.deck1.deal())

    def reset_game(self):
        print("Starting game, shuffling and dealing deck...")
        self.deck1.clear()
        self.deck1.fill()
        self.deck1.shuffle()
        self.deal()

    def playing(self):
        self.reset_game()
        time.sleep(4)
        self.player1.card[0].print_name()
        amt = self.player1.bet()
        print("Player betting", amt, "tokens. Odds are 1:1")
        self.table.add_tokens(amt)
        time.sleep(1)
        print("Dealer has: ", self.dealer1.card[0].print_name())
        if self.dealer1.card[0].getValue() >

