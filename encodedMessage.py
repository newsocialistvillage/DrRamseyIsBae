

with open("colors.ppm") as fn:
    file_object = fn.readlines()

fn.close()

L = file_object[3:]  # start with the fourth line, first three lines are useless for the operation below

# insert message below

width = 256.0
height = 256.0

wd = input("Please input a three lettered-word: ")
list(wd)

print(L[:3])
num1 = ord('a') - ord('a') + 1
num0 = ord('c') - ord('c') + 3
num2 = ord('t') - ord('t') + 20

L = list(map(int, L))

i = 0
L[i] += num0
L[i + 1] += num1
L[i + 2] += num2


L[i + int(width*height/2)] += num0
L[i + int(width*height/2 + 1)] += num1
L[i + int(width*height/2 + 2)] += num2


L = ['{:.0f}'.format(x) for x in L]
for i in range(len(L)):
    L[i] = L[i] + "\n"

print(L[:3])

with open('colors1.ppm', 'w') as fh:
        fh.write("P3\n")
        fh.write("256 256\n")
        fh.write("255\n")
        for i in range(len(L)):
            fh.write(L[i])

fh.close()