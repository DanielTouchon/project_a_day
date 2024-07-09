from random import choice

def rock_paper_scissors():
    possibilities = ["rock","paper","scissors"]
    user_choice = ""
    pc_choice = choice(possibilities)
    
    while user_choice not in possibilities:
        user_choice = input("\"Rock\"(r), \"paper\"(p) or \"scissors\"(s)? ").lower().strip()
        if user_choice == pc_choice:
            return f"{user_choice} x {pc_choice}\nIt's a draw!"
        
        if user_choice == "rock":
            if pc_choice == "paper":
                return f"{user_choice} x {pc_choice}\nPC wins!"
            else:
                return f"{user_choice} x {pc_choice}\nYou win!"
        
        if user_choice == "paper":
            if pc_choice == "rock":
                return f"{user_choice} x {pc_choice}\nYou win!"
            else:
                return f"{user_choice} x {pc_choice}\nPC wins!"
            
        if user_choice == "scissors":
            if pc_choice == "rock":
                return f"{user_choice} x {pc_choice}\nYou win!"
            else:
                return f"{user_choice} x {pc_choice}\nPC wins!"
            
print(rock_paper_scissors())