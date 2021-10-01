#Seat Plan arrangement
import numpy as np
import time
import math
import random

class Relation:
    def __init__(self, person_x, person_y, happiness, id):
        self.person_x = person_x
        self.person_y = person_y
        self.happiness = happiness
        self.id = id ##Indexing value

    def __repr__(self):
        return str(self)

        
## initializing all the relations
def collectRelations(state_space):
    rls = []
    for [x,y,h,g] in state_space:
        rls.append(Relation(x,y,h,g))
    return [Relation.happiness for Relation in rls]
        
## encoding
#initialize seating
def seating():
    seats = ["_","_","_","_","_"]
    people = ['A','B','C','D','E']
    seats = people
    return seats



def happiness_calc():
    seats = seating()
    
    for i in range(len(seats)):
        if i-1 < 0:
            a
        else:
            a = seats[i-1]
            b = seats[i]
            c = seats[i+1]
        

    return happiness


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def hex2gray(person):
    h_num = int(person, 2)
    h_num ^= (h_num >> 1)
    gray = bin(h_num)[2:]   
    return gray

def value2gray(inum):
    inum = int(inum)
    b_num = np.binary_repr(inum)
    b_num = int(b_num, 2)
    b_num ^= (b_num >> 1)
    gray = bin(b_num)[2:]   
    return gray


def gray2value(gray):
    gnum = int(gray, 2)
    mask = gnum
    while mask != 0:
        mask >>= 1
        gnum ^= mask
    value = int(gnum)
    return value



if __name__ == '__main__':
    state_space = [["A", "B", 20, 1],
    ["A", "C", 20, 2],
    ["A", "D", 30, 3],
    ["A", "E", 25, 4],
    ["B", "A", 20, 5],
    ["B", "C", 50, 6],
    ["B", "D", 20, 7],
    ["B", "E", 5, 8],
    ["C", "A", 10, 9],
    ["C", "B", 10, 10],
    ["C", "D", 100, 11],
    ["C", "E", 10, 12],
    ["D", "A", 50, 13],
    ["D", "B", 5, 14],
    ["D", "C", 10, 15],
    ["D", "E", -5, 16],
    ["E", "A", -50, 17],
    ["E", "B", -30, 18],
    ["E", "C", -100, 19],
    ["E", "D", -10, 20]
    ]
    print(collectRelations(state_space))
    print(seating())