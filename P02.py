## Evolutionary Computing 
import time
import numpy as np
import math
## Binary to Gray
def btg():
    inum = int(input("Please input a positive integer: "))
    choice = input("Please input 1 to get binary, please into 0 to get gray code: ")
    if choice == 1:
        b_num = np.binary_repr(inum)
        bnum_list = list(b_num)
    else:
        b_num = np.binary_repr(inum)
        print(b_num)
        b_num = int(b_num, 2)
        b_num ^= (b_num >> 1)
        g_num = bin(b_num)[2:]
        gnum_list = list(g_num)
    return g_num    




## Hamming distance
from scipy.spatial.distance import hamming

def hmg():
    inum = int(input("Please input a positive integer: "))
    choicea = input("Please input 1 to get binary, please into 0 to get gray code: ")
    if choicea == 1:
        b_num = np.binary_repr(inum)
        y = list(b_num)
    else:
        b_num = np.binary_repr(inum)
        print(b_num)
        b_num = int(b_num, 2)
        b_num ^= (b_num >> 1)
        g_num = bin(b_num)[2:]
        x = list(g_num)
    inum = int(input("Please input a positive integer: "))
    choiceb = input("Please input 1 to get binary, please into 0 to get gray code: ")
    if choiceb == 1:
        b_num = np.binary_repr(inum)
        y2 = list(b_num)
    else:
        b_num = np.binary_repr(inum)
        print(b_num)
        b_num = int(b_num, 2)
        b_num ^= (b_num >> 1)
        g_num = bin(b_num)[2:]
        x2 = list(g_num)
    
    print(x)
    print(x2)
    
    if choicea and choiceb == 1:
        result = hamming(x, x2) * len(x)  
    elif choicea and choiceb == 0:
        result = hamming(y, y2) * len(y)
    else:
        result = "error"
    return result
    
## Plot the hamming distance between 1-10 in binary

import matplotlib.pyplot as plt

b_array = []

def bdist():
    for i in range(10):
        bnum = np.binary_repr(i)
        bnum_temp = list(bnum)
        b_array.append(bnum_temp)
        print(b_array)
    i=0
    h_array = []
    for i in range(len(b_array) - 1):
        ##compare each element to its next different, get the hamming distance and store it into an array
        a = b_array[i]
        b = b_array[i+1]
        if len(a) == len(b):
            x = len(a)
        else:
            a.insert(0, '0')
            x = len(a)
        h_array.append((hamming(a, b) * x))

    plt.plot(h_array)
    plt.ylabel("Distance")
    plt.xlabel("Integer")
    plt.show()
        
def gdist():
    g_array = []
    for i in range(10):
        b_num = np.binary_repr(i)
        b_num = int(b_num, 2)
        b_num ^= (b_num >> 1)
        g_num = bin(b_num)[2:]
        gnum_temp = list(g_num)
        g_array.append(gnum_temp)
        print(g_array)
    i=0
    h_array = []
    for i in range(len(g_array) - 1):
        ##compare each element to its next different, get the hamming distance and store it into an array
        a = g_array[i]
        b = g_array[i+1]
        if len(a) == len(b):
            x = len(a)
        else:
            a.insert(0, '0')
            x = len(a)
        h_array.append((hamming(a, b) * x))

    plt.plot(h_array)
    plt.ylabel("Distance")
    plt.xlabel("Integer")
    plt.show()

##Genetic Algorithm

##Given a length of x and y split the rectangle into as many equaly squares as possible with as large of squares as possible
##Maximize x of square, minimize empty spaces left

scores = []
xs = []
def fitness_fcn(x):   
    if x == 0:
        return 0
    else:
        squares = (w*h)/(x**2)
        rsquares = math.floor(squares)
        prescore = squares - rsquares
        fitness = float(1 - prescore)
        ## The closer the score is to 1 the better the fit (the less leftover space)
    return fitness


#ListToString
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

## Encoding
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

#population intialization
import random
def generatePopulation(pop_size, pop_min, pop_max):
    population = []
    for i in range(pop_size):
        population.append(float(random.randint(pop_min, pop_max)))
    return population

#Parent Selection
def selectParents(chromosomes, pop_size):
    parent_pairs = []
    for i in range(int(pop_size/2)):
        p = []
        for y in range(2):
            x = random.randint(0, (len(chromosomes)-1))
            p.append(chromosomes[x])      
        parent_pairs.append(p)    
    return parent_pairs

#Crossover
def crossover(parent_pairs):
    gOffsprings = []
    offsprings = []
    for i in range(len(parent_pairs)):
        chr_length = 4
        g_parentsa = list(value2gray(parent_pairs[i]))
        g_parentsb = list(value2gray(parent_pairs[i]))
        k = random.randint(0, chr_length-2) ## get the random crossover point
        for x in range(k, len(g_parentsa)):
            g_parentsa[x], g_parentsb[x] = g_parentsb[x], g_parentsa[x]
        g_parentsa = ''.join(g_parentsa)
        g_parentsb = ''.join(g_parentsb)
        gOffsprings.append(g_parentsa)
        gOffsprings.append(g_parentsb)
    for i in range(len(gOffsprings)):
        offsprings.append(gray2value(gOffsprings[i]))
    return offsprings

#Mutation 
def mutate(chromosome, p_mutation):
    g_chrome = list(value2gray(chromosome))
    mutated = []
    mutated_ = ""
    for i in range(len(g_chrome)):
        m = random.uniform(0,1)
        if m > p_mutation:
            g_chrome[i] = 1
        else: 
            g_chrome[i] = 0
        mutated.append(str(g_chrome[i]))
    mutated_ = listToString(mutated)
    mutated = gray2value(mutated_)
    return mutated

#Repeat until Termination
def findOverallDistance(chromosomes):
    fit_list = []
    distances = []
    overall_distance = 0
    for i in range(len(chromosomes)):
        fit_list.append(fitness_fcn(chromosomes[i]))
    fit_list.sort()
    for i in range(len(fit_list)):
        d_temp = (fit_list[i]*100)
        distances.append(d_temp)
    for i in range(len(distances)-1):
        a = distances[i]
        b = distances[i+1]
        overall_distance += (b-a)
        

    return overall_distance

if __name__ == '__main__':
    pop_size = 10
    w = 20
    h = 15
    pop_min = 1
    pop_max = 10
    curr_iter = 0
    max_iter = 100
    min_overalldistance = 0.5
    p_mutation = 0.05
    population = []
    population.append(generatePopulation(pop_size, pop_min, pop_max))
    while (curr_iter < max_iter and findOverallDistance(population[-1]) > min_overalldistance):
        curr_iter +=1 
        parents = selectParents(population[-1], len(population[-1]))
        offsprings = []
        for p in parents:
            new_offsprings = crossover(p)
            for o in new_offsprings:
                offsprings.append(o)
        mutated = [mutate(offspring, p_mutation) for offspring in offsprings]
        population.append(mutated)
        print(curr_iter,findOverallDistance(population[-1]),sum([fitness_fcn(x) for x in population[-1]]))
    print(population[-1])


