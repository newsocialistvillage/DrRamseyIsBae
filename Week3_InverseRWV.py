
'''

author@ Zhengqi(Charles) Yang

created@ March.23rd, 2018


'''


file = open('balls_RWV1.ppm')

typeFile = file.readline()


WandH = file.readline()
t = WandH.split()
width = int(t[0])
height = int(t[1])

numberofcolors = file.readline()

Colors = file.read()
file.close()
Pixel = list(map(float, Colors.split()))
topPixel = []
botPixel = []
BefAveHeight = []
leftPixel = []
rightPixel = []
BefAveWidth = []

for i in range(int(3 * height * width / 2)):
    topPixel.append(Pixel[i] + Pixel[int((3 * width * height / 2) + i)])
    botPixel.append(2 * Pixel[i] - topPixel[i])

for j in range(int(height / 2)):
    for k in range(width):
        BefAveHeight.append(topPixel[3 * k + 3 * width * j])
        BefAveHeight.append(topPixel[3 * k + 3 * width * j + 1])
        BefAveHeight.append(topPixel[3 * k + 3 * width * j + 2])
    for k in range(width):
        BefAveHeight.append(botPixel[3 * k + 3 * width * j])
        BefAveHeight.append(botPixel[3 * k + 3 * width * j + 1])
        BefAveHeight.append(botPixel[3 * k + 3 * width * j + 2])


for i in range(height):
    for j in range(int(width / 2)):
        leftPixel.append(BefAveHeight[3 * i * width + 3 * j] + BefAveHeight[3 * i * width + 3 * j + 3 * width // 2])
        rightPixel.append(2 * BefAveHeight[3 * i * width + 3 * j] - leftPixel[3 * i * width // 2 + 3 * j])
        leftPixel.append(
            BefAveHeight[3 * i * width + 3 * j + 1] + BefAveHeight[3 * i * width + 3 * j + 3 * width // 2 + 1])
        rightPixel.append(2 * BefAveHeight[3 * i * width + 3 * j + 1] - leftPixel[3 * i * width // 2 + 3 * j + 1])
        leftPixel.append(
            BefAveHeight[3 * i * width + 3 * j + 2] + BefAveHeight[3 * i * width + 3 * j + 3 * width // 2 + 2])
        rightPixel.append(2 * BefAveHeight[3 * i * width + 3 * j + 2] - leftPixel[3 * i * width // 2 + 3 * j + 2])

for i in range(height):
    for j in range(int(width / 2)):
        BefAveWidth.append(leftPixel[3 * j + 3 * i * width // 2])
        BefAveWidth.append(leftPixel[3 * j + 3 * i * width // 2 + 1])
        BefAveWidth.append(leftPixel[3 * j + 3 * i * width // 2 + 2])

        BefAveWidth.append(rightPixel[3 * j + 3 * i * width // 2])
        BefAveWidth.append(rightPixel[3 * j + 3 * i * width // 2 + 1])
        BefAveWidth.append(rightPixel[3 * j + 3 * i * width // 2 + 2])

newfile = open('balls_RWV_inversed.ppm', "w")

newfile.write("P3\n")
newfile.write(str(width) + " " + str(height) + "\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(int(BefAveWidth[3 * i * width + 3 * j])) + " ")
        newfile.write(str(int(BefAveWidth[3 * i * width + 3 * j + 1])) + " ")
        newfile.write(str(int(BefAveWidth[3 * i * width + 3 * j + 2])) + " ")
    newfile.write("\n")

newfile.close()