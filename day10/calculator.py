from art import logo
import os
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def call_op(op,x,y):
    if op == '+':
        return add(x,y)
    if op == '-':
        return subtract(x,y)
    if op == '*':
        return multiply(x,y)
    if op == '/':
        return divide(x,y)
    
def calculator():
    keep_going = True
    while keep_going:
        print(logo)
        fn = int(input())
        op = str(input()).lower()
        sn = int(input())
        
        if op == 'x':
            print("Calculator closed.")
            keep_going = False
        else:
            print(call_op(op,fn,sn))
            sleep(5)
            cls()

calculator()