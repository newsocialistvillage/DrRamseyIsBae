'''

author@Zhengqi Yang


'''


def dedupe_adjacent(alist, num):
         for i in range(len(alist) - 1, 0, -1):
             if alist[i] == alist[i-1]:
                del alist[i]

#with open("pos1colors.ppm") as fn:
fn = open("rwv1colors.txt")
typeFile = fn.readlines()

fn.close()
wh = typeFile[1].split()
originalwidth = int(wh[0])
originalheight = int(wh[1])

L = typeFile[3:]  # start with the fourth line, first three lines are useless for the operation below

print(L[:3])

print("Please enter a threshold:")
threshold = float(input())

L = list(map(float, L))

print(L[:3])

totalCount = 0
counter = 0

for i in range(len(L)):
    if abs(L[i]) <  0.00001:
        totalCount += 1


print(totalCount)

totalCount = 0

for i in range(len(L)):
    if abs(L[i]) < (0 + threshold):
        L[i] = 0
        totalCount += 1

print(totalCount)

totalCount = 0

i = 1
while i < len(L):
    counter = 1
    if L[i] == 0:
        while L[i] == L[i+1]:
            counter += 1
            L.pop(i)

        L.insert(i+1, counter)

    i += 1

print(L)

for i in range(len(L)):
    if abs(L[i]) <  0.00001:
        totalCount += 1

print("the total count is " + str(totalCount))

L = ['{:.5f}'.format(x) for x in L]

with open('zeroedOut.ppm', 'w') as fh:
    fh.write("P3\n")
    fh.write("256 256\n")
    fh.write("255\n")
    for i in range(len(L)):
        if L[i] == 0:
            for j in range(L[i+1]+1):
                fh.write("0\n")
    else:
        fh.write(L[i])

fh.close()

