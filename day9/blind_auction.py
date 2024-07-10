import locale,os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def blind_auction():
    locale.setlocale(locale.LC_ALL, '')
    bidders = []
    one_more_bidder = True
    while one_more_bidder:
        bidders.append({
            "name": input("What's your name? "),
            "bid": int(input("Whats's your bid? "))
        })
        
        one_more_bidder = True if input("Is there another bidder? \'y\' or \'n\' ") == 'y' else False
        cls()
    
    winner = sorted(bidders,key=lambda b: b["bid"],reverse=True)[0]
    
    return f"Winner is {winner["name"]} with a {locale.currency(winner["bid"])} bid."

print(blind_auction())