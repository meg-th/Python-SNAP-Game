from random import randint, shuffle
from functools import reduce
import operator

class Game:
    # Instantiates new games with all the required objects
    def __init__(self):
        self.__game_cards = Deck()
        self.__discard_pile = []
        self.__player_1 = Player('Player 1')
        self.__player_2 = Player('Player 2')
    
    def play(self):
        self.__game_cards.set_deck()
        self.__player_1.player_hand, self.__player_2.player_hand = self.__game_cards.split_deck()
        game_sequence = reduce(operator.add, zip(self.__player_1.player_hand, self.__player_2.player_hand)) # Creates an alternating list of the values held in both players decks. 

        for index, elem in enumerate(game_sequence):
            if len(self.__discard_pile) > 0:
                print(f'{index + 1} {elem}')
                prev_elem = game_sequence[index - 1]
                self.__discard_pile.append(prev_elem)
                if (elem['value'] == prev_elem['value'] or elem['suit'] == prev_elem['suit']):
                    if randint(0,1) == 1: # The person who calls snap is determined randomly.
                        round_winner = self.__player_1
                    else:
                        round_winner = self.__player_2
                    print(f'{round_winner.name} has called SNAP on the match betweeen {elem} and {prev_elem}!')
                    [round_winner.cards_won.append(i) for i in self.__discard_pile]
                    self.__discard_pile.clear()
            else:
                print(f'{index + 1} {elem}')
                self.__discard_pile.append(elem)
        self.__declare_winner()
      
    def __declare_winner(self):
        if len(self.__player_1.cards_won) > len(self.__player_2.cards_won):
            winner, loser = self.__player_1, self.__player_2
        else:
            winner, loser = self.__player_2, self.__player_1
        string = '''
             __| |_____________________________________________________| |__
            (__   _____________________________________________________   __)
               | |                                                     | |
               | |                                                     | |
               | |  {w} is the winner - {w_cards} cards won!             | |
               | |                                                     | |
               | |  {l} is the loser - only {l_cards} cards won!         | |
               | |                                                     | |
             __| |_____________________________________________________| |__
            (__   _____________________________________________________   __)
               | |                                                     | |
            '''.format(w=winner.name, w_cards=len(winner.cards_won), l=loser.name, l_cards=len(loser.cards_won))
        print(string)

class Deck: 
    # Instantiates a new deck object, to maintain the state of all the cards used in the game. 
    def __init__(self):
        self.deck = []

    def set_deck(self):
        suits = ['HEARTS', 'SPADES', 'CLUBS', 'DIAMONDS']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        num_decks = int(input("How many decks of cards should the players use?\n"))

        # If user input is greater than 0, then set game deck as a list of dictionaries.
        if num_decks > 0:
            for i in range(num_decks):
                for x in suits:
                    for y in values:
                        self.deck.append({
                            'value': y,
                            'suit': x
                        })
            # Deck is shuffled here and returned to the Game object. 
            return shuffle(self.deck)
        else: 
            raise Exception("You can't enter a number smaller than 0! Please try again.")
      
    def split_deck(self):
        return self.deck[:(len(self.deck)//2)], self.deck[(len(self.deck)//2):]

class Player:
    # Instantiates player objects, to maintain the state of cards held by individual players. 
    def __init__(self, name):
        self.name = name
        self.player_hand = []
        self.cards_won = []