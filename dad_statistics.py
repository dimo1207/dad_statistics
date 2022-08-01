import math
from random import *
import matplotlib.pyplot as plt
import numpy as np

probability = 100  # Ex: for 1/100 odds, enter 100 here
batch = 1000000 # total number of rolls used to test the theory
cutoff = .5 # Statistical midpoint; half of all successful rolls occur at or below this number


# Ex: for 1/100 odds, the calculation for the midpoint looks like: .99^y = 0.5
# To find y, the calculation needs to be: log [base:0.99] (0.5) = y
# The following code makes this calulation for any probability:

base = 1 - (1/probability) # the probability of the roll being unsuccessful; necessary for the calculation
exponent = math.log(cutoff, base) # Number of rolls needed to reach midpoint

n = 1 # roll number
successList = []
for x in range(1, batch):
    target = randint(1, probability)
    roll = randint(1, probability)

    if roll == target:
        successList.append(n)
        n = 1
    else:
        n += 1

total = 0
half = 0
for x in successList:
    total += x
    if x <= exponent: # exponent indicates the number of rolls to reach the midpoint -- where half of all rolls reside below, and half above
        half += 1

print(f"\nPercentage of successful rolls occuring before or at the halfway point (~{round(exponent)} rolls for 1 in {probability} odds):")
print(half/len(successList))
print(f"\nFewest attempts required for successful roll: \n{min(successList)}\n")
print(f"Greatest number of attempts until successful roll: \n{max(successList)}\n")

frequency = []
for i in successList:
    frequency.append((i, successList.count(i)))

frequency = set(frequency)
y = 1
for x in frequency:
    # if x[1] > 1:
    #     print(x)
    if x[1] > y:
        y = x[1]
        
for x in frequency:
    if x[1] == y:
        print(f"Most frequent successful roll + frequency: \n{x}")

roll = []
freq = []
for i in successList:
    roll.append(i)
    freq.append(successList.count(i))
plt.scatter(roll, freq)
plt.xlabel("Roll")
plt.ylabel("Frequency")
plt.show()