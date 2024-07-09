from random import choice,shuffle

def password_generator():
    letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

    print("Welcome to Password Generator\n")
    num_letters = int(input("How many letters do you want your password to contain? "))
    num_symbols = int(input("How many symbols do you want your password to contain? "))
    num_integers = int(input("How many integers do you want your password to contain? "))
    
    password_chars = []
    
    for _ in range(num_letters):
        password_chars.append(choice(letters))
    
    for _ in range(num_symbols):
        password_chars.append(choice(symbols))
    
    for _ in range(num_integers):
        password_chars.append(choice(integers))
        
    shuffle(password_chars)
    
    return "Your password: " + "".join(password_chars)

print(password_generator())