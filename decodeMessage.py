with open("colors1.ppm") as fn:
    file_object = fn.readlines()

fn.close()

with open("colors.ppm") as fn1:
    file_object1 = fn1.readlines()

fn1.close()

L = file_object[3:]  # start with the fourth line, first three lines are useless for the operation below
L1 = file_object1[3:]
L = list(map(int, L))
L1 = list(map(int, L1))
L2 = []
allothers = []
print("hi my name is")
print(" L is ", L[:3])
print("L1 is ", L1[:3])
for idx in range(len(L)):
    num = L[idx] - L1[idx]
    if num != 0:
        L2.append(num)
    else:
        allothers.append(num)

#print(L,"\n",L1,"\n",L2)
#print("allothers:", allothers)
print("The decoded message is:")

L3 = []

for i in range(len(L2)):
    char = chr(L2[i] + ord('a') - 1)
    L3.append(char)


print(L3)
for i in range(len(L3)):
    print(L3[i])

