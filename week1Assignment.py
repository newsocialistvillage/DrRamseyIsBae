"""
Author@Zhengqi(Charles) Yang

Date: Jan.31st, 2018

Week 1 Assignment

read in a list of numbers from the user (input)
average them (is converting input into an integer int)
--- average every pair in order

"""

numList = []

# input numbers into a list
numList = [int(x) for x in input().split()]

print(numList)

# average equals to sum/length
average = sum(numList) / len(numList)

print("Here is the average of the list of numbers: ")
print(average)

numList2 = []

numList2 = [(a + b) / 2 for a, b in zip(numList[::2], numList[1::2])]

print("Here is the new list that we have derived: ")
print(numList2)


