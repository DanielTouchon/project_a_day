from guess_the_number import Guesser

level = input("What level do you want to play in?\nType \'hard\',\'medium\' or \'easy\': ")
new_game = Guesser(level)
new_game.play()