from models import Game

def main():
    while True:
        # Loop will continue to run until the user explicitly enters the word 'no' into the terminal. 
        answer = input("Would you like to play a game of SNAP!? Please type in 'yes' or 'no':\n")
        if answer == 'yes':
            print("\n************** Welcome to a NEW game of SNAP! ************** \n")
            game = Game()
            game.play()
        elif answer == 'no':
            break
        else:
            print("Sorry, we don't understand this response.\n")
main()