def treasure_island():
    
    print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
    
    first_choice = ""
    second_choice = ""
    third_choice = ""
    
    while first_choice not in ["right","r","left","l"]:
        first_choice = input("You are at a cross roads. Where do you want to go? Type \"left\" or \"right\": ").lower()
    
    if first_choice == "right" or first_choice == "r":
        return "You get kidnappd by Game Over"
    
    else:
        while second_choice not in ["swim","s","wait","w"]:
            second_choice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across the lake: ").lower()
        
        if second_choice == "swim" or second_choice == "s":
            return "A nameless gargantuan beast swallows you whole!\nGame Over."
        
        else:
            while third_choice not in ["red","r","blue","b","yellow","y"]:
                third_choice = input("You arrive at the island unharmed. There is a house with three doors. Choose \"red\", \"blue\" or \"yellow\": ").lower()
            
            if third_choice == "yellow" or third_choice == "y":
                return "Nice!!\nYou found the treasure!"
            else:
                return "You enter a room full of beasts!\nGame Over!"

print(treasure_island())