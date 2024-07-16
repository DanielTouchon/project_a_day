from random import randint

class Guesser:
    def __init__(self,level):
        if str(level).lower() == 'hard':
            self.attempts_left = 5
        elif str(level).lower() == 'medium':
            self.attempts_left = 7
        elif str(level).lower() == 'hard':
            self.attempts_left = 10
        self.numbers_tried = []
        self.final_number = randint(1,100)
        
    def play(self):
        print(f"Welcome to Guess the Number!\nYou have {self.attempts_left} attempts.")
        new_try = ''
        keep_going = True
        while keep_going:
            new_try = int(input("Guess the number: "))
            
            if new_try > self.final_number:
                print("Too High!")
                self.attempts_left -= 1
            elif new_try < self.final_number:
                print("Too Low!")
                self.attempts_left -= 1
            else:
                print(f"The number was {self.final_number}\nYou Won!!")
            
            if self.attempts_left == 0:
                keep_going = False
                print(f"The number was {self.final_number}\nYou Lost!!")
                
            self.numbers_tried.append(new_try)