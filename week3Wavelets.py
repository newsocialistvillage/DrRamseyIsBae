'''

author@ Zhengqi(Charles) Yang

created@ Feb.6th 2018

hint:

i = idx(0, 0, 2)
j = idx(1, 0 ,2)
and then average

When it gets bigger, it changes a little bit

a = {1,2,3}
b = {3,4,5}
a = list(b)

'''


def idx(wt, ht, maxwidth):
    return ht * maxwidth * 3 + wt * 3


# function for only storing every other element
def altelement(l):
    return l[::2]

def average(a , b):
    return (a+b)/2


ppmFile = open("balls.ppm")

format = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
max = ppmFile.readline()
p = []


for x in ppmFile:
    l = x.split()
    for a in l:
        p.append(int(a))

r = p[0: len(p): 3]
g = p[1: len(p): 3]
b = p[2: len(p): 3]
g = p[1: len(p): 3]
b = p[2: len(p): 3]



ppmFile = open("balls.ppm")

format = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
maxval = ppmFile.readline()
p = []

for x in ppmFile:
    l = x.split()
    for a in l:
        p.append(int(a))

r = p[0: len(p): 3]
g = p[1: len(p): 3]
b = p[2: len(p): 3]

r = list(map(int, r))
g = list(map(int, g))
b = list(map(int, b))

offsetR = [(a + b) / 2 - b for a, b in zip(r[::2], r[1::2])]
offsetG = [(a + b) / 2 - b for a, b in zip(g[::2], g[1::2])]
offsetB = [(a + b) / 2 - b for a, b in zip(b[::2], b[1::2])]

avgR = [(a + b) / 2 for a, b in zip(r[::2], r[1::2])]
avgG = [(a + b) / 2 for a, b in zip(g[::2], g[1::2])]
avgB = [(a + b) / 2 for a, b in zip(b[::2], b[1::2])]

AvgRGB = [j for i in zip(avgR, avgG, avgB) for j in i]
offsetRGB = [j for i in zip(offsetR, offsetG, offsetB) for j in i]

s = 0
q = int(widthHeight[0]) // 2 * 3  # width x128
columnCounter = 0
newList = []
for columnCounter in range(0, int(widthHeight[1])):  # height x128
    for i in range(s, q):
        newList.append(AvgRGB[i])
    for i in range(s, q):
        newList.append(offsetRGB[i] + 127.5)  # +127.5
    s += int(widthHeight[0]) // 2 * 3
    q += int(widthHeight[0]) // 2 * 3


Rr = []
Bb = []
Gg = []

offsetRl = []
offsetGl = []
offsetBl = []

width = int(widthHeight[0])

for i in range(int(int(widthHeight[1]) / 2)):  # here i is which set of rows
    # print("final:",i,i*width*3*2)
    for j in range(int(width)):  # j is which color in that row
        # print(j,i*width*3*2 + 3*j)
        firstR = i * (width) * 3 * 2 + 3 * j
        firstG = firstR + 1
        firstB = firstR + 2
        secondR = i * (width) * 3 * 2 + 3 * j + 3 * (width)
        secondG = secondR + 1
        secondB = secondR + 2

        rl = int((newList[firstR] + newList[secondR]) / 2)
        bl = int((newList[firstB] + newList[secondB]) / 2)
        gl = int((newList[firstG] + newList[secondG]) / 2)

        offsetRR = rl - newList[secondR] + 127.5
        offsetBB = bl - newList[secondB] + 127.5
        offsetGG = gl - newList[secondG] + 127.5

        Rr.append(rl)
        Bb.append(bl)
        Gg.append(gl)

        offsetRl.append(offsetRR)
        offsetGl.append(offsetGG)
        offsetBl.append(offsetBB)

        # print (i, j, secondr)
        # print(firstr,firstg,firstb,secondr,secondg,secondb)

newRGB = [j for i in zip(Rr, Gg, Bb) for j in i]
offsetRGB = [j for i in zip(offsetRl, offsetGl, offsetBl) for j in i]
# print (offsetRl)

RGB = newRGB + offsetRGB

# print (Rr)


newW = int(widthHeight[0])
newH = int(widthHeight[1])
newPPM = open("balls_RWV1.ppm", "w")
newPPM.write("%s" % (format))
newPPM.write("%d %d\n" % (newW, newH))
newPPM.write(maxval)

x = 0

while (x < len(RGB)):
    newPPM.writelines("%d\n" % RGB[x])
    x = x + 1

newPPM.close()
ppmFile.close()
