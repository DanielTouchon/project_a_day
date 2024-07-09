import locale

def calculate_tip():
    total_bill = float(input("What's the bill? "))
    tip_percentage = int(input("What tip percentage do you want to pay? (10,12,15) "))
    num_people = int(input("How many people are splitting the bill? "))
    
    bill_plus_tip = total_bill * (1 + (tip_percentage/100))
    bill_per_person = bill_plus_tip/num_people
    
    locale.setlocale(locale.LC_ALL, '')
    
    print(locale.currency(bill_per_person))
    
calculate_tip()