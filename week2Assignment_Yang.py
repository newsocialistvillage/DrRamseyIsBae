"""

Created on Jan.30th, 2018

author@Zhengqi(Charles) yang

class@Python Practicum

Week2 Assignment Blurring an Image, Into the PPM Format

Read a PPM file, read in all the numbers
throw out every other color
average all the numbers and output a new image half the width.

"""


# functions for outputting the ppm file


# function for only storing every other element
def altElement(l):
    return l[::2]


fileName = 'colors.ppm'

with open("colors.ppm") as fn:
    file_object = fn.readlines()

fn.close()

L = file_object[3:]  # start with the fourth line, first three lines are useless for the operation below

# slice the list into three RGB lists
R = L[0:len(L):3]
G = L[1:len(L):3]
B = L[2:len(L):3]

# throw out every other element
# altElement(R)
# altElement(G)
# altElement(B)

# converting to ints
R = list(map(int, R))
G = list(map(int, G))
B = list(map(int, B))

# zip to average every single pair of num
newR = [(a + b) / 2 for a, b in zip(R[::2], R[1::2])]
newG = [(a + b) / 2 for a, b in zip(G[::2], G[1::2])]
newB = [(a + b) / 2 for a, b in zip(B[::2], B[1::2])]

# add up all three new lists together
L2 = []

for i in range(0, len(newR), 1):
    L2.append(newR[i])
    L2.append(newG[i])
    L2.append(newB[i])

# test printing new ppm list
print(L2[:3])

# turning l2 into a list of str
L2 = ['{:.0f}'.format(x) for x in L2]
for i in range(len(L2)):
    L2[i] = L2[i] + "\n"

with open('checkers.ppm', 'w') as fh:
        fh.write("P3\n")
        fh.write("178 178\n")
        fh.write("255\n")
        for i in range(len(L2)):
            fh.write(L2[i])

fh.close()
