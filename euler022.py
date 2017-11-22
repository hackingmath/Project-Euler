'''Project Euler Problem #22
Names Scores
November 21, 2017'''
from ast import literal_eval


mylist = ["","ARYAN","MARC","PETER"]

def alphabetize(listName):
    '''alphabetizes the items in a list'''
    return sorted(listName)

def numval(string):
    alpha = '_abcdefghijklmnopqrstuvwxyz'
    total = 0 #value
    for letter in string:
        total += alpha.index(letter.lower())
    return total

def placeval(string,listName):
    return listName.index(string) + 1

def nameScore(string,listName):
    return placeval(string,listName) * numval(string)


with open('names.txt') as f:
    for line in f:
        namelist = list(literal_eval(line))

namelist = alphabetize(namelist)
#print(namelist[:10])

total_scores = 0

for name in namelist:
    total_scores += nameScore(name,namelist)

print(total_scores)
    
#correct: 871198282
