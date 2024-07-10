def caesar_cipher():
    initial_word = input("Type the word you want to encode: ")
    shift = int(input("Type the shift: ")) % 26
    
    new_word = ""
    for letter in initial_word:
        if letter.isalpha():
            new_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
            new_word += new_letter
        else:
            new_word += letter
    
    return new_word

print(caesar_cipher()) 