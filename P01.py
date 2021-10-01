from random import *
def tossCoin():
    result = randint(0,1)
    if result == 1:
        coin = "heads"
    else:
        coin = "tails"
    return coin

def fibonnaci():
    seq = [0,1]
    next= 0
    last = 0
    new = 0
    ## index variables
    i = 0 
    a = 0
    b = 1
    cont = 1
    while cont == 1:
        for i in range(5):
            last = seq[a]
            next = seq[b]
            new = last + next
            seq.append(new)
            a +=1
            b +=1
            print(seq)
        cont = int(input("Press 1 to continue, Press 0 to exit: "))
    return seq

def chooseFromThree():
    prize_num = randint(0,9)
    choice = input("Please input A, B or C: ")
    if 0 >= prize_num <= 1:
        prize = "A"
    elif 2 >= prize_num <= 6:
        prize = "B"
    elif 7 >= prize_num <= 9:
        prize = "C"
    else:
        print("invalid input")
    if choice == prize:
        print("BINGO! Pog")
    else:
        print("No prize pepeHands")
        print("Prize is " + prize)
    return prize


print(chooseFromThree())
print(tossCoin())
print(fibonnaci())
