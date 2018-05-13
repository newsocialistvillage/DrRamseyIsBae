
file = open('balls_RWV1.ppm')

typeoffile = file.readline()

print(typeoffile)
WandH = file.readline()
t = WandH.split()
width = int(t[0])
height = int(t[1])

print("width is: ", width, "height is: ", height)

numberofcolors = file.readline()

print("How many color pixels: ", numberofcolors)

Colors = file.read()
file.close()
Pixel = list(map(int, Colors.split()))
print(Pixel)
newPixel = []
tempPixel = []
newPixelaveH = []

for i in range(height):
    for j in range(int(width / 2)):
        newPixel.append((Pixel[3 * i * width + 6 * j] + Pixel[3 * i * width + 6 * j + 3]) / 2)
        tempPixel.append(
            (Pixel[3 * i * width + 6 * j] + Pixel[3 * i * width + 6 * j + 3]) / 2 - Pixel[3 * i * width + 6 * j + 3])

        newPixel.append((Pixel[3 * i * width + 6 * j + 1] + Pixel[3 * i * width + 6 * j + 4]) / 2)
        tempPixel.append((Pixel[3 * i * width + 6 * j + 1] + Pixel[3 * i * width + 6 * j + 4]) / 2 - Pixel[
            3 * i * width + 6 * j + 4])

        newPixel.append((Pixel[3 * i * width + 6 * j + 2] + Pixel[3 * i * width + 6 * j + 5]) / 2)
        tempPixel.append((Pixel[3 * i * width + 6 * j + 2] + Pixel[3 * i * width + 6 * j + 5]) / 2 - Pixel[
            3 * i * width + 6 * j + 5])
    newPixel.extend(tempPixel)
    tempPixel.clear()

for m in range(int(height / 2)):
    for n in range(width):
        newPixelaveH.append((newPixel[2 * m * 3 * width + 3 * n] + newPixel[2 * m * 3 * width + 3 * n + 3 * width]) / 2)
        tempPixel.append(newPixel[2 * m * 3 * width + 3 * n] - (
                    newPixel[2 * m * 3 * width + 3 * n] + newPixel[2 * m * 3 * width + 3 * n + 3 * width]) / 2)

        newPixelaveH.append(
            (newPixel[2 * m * 3 * width + 3 * n + 1] + newPixel[2 * m * 3 * width + 3 * n + 3 * width + 1]) / 2)
        tempPixel.append(newPixel[2 * m * 3 * width + 3 * n + 1] - (
                    newPixel[2 * m * 3 * width + 3 * n + 1] + newPixel[2 * m * 3 * width + 3 * n + 3 * width + 1]) / 2)

        newPixelaveH.append(
            (newPixel[2 * m * 3 * width + 3 * n + 2] + newPixel[2 * m * 3 * width + 3 * n + 3 * width + 2]) / 2)
        tempPixel.append(newPixel[2 * m * 3 * width + 3 * n + 2] - (
                    newPixel[2 * m * 3 * width + 3 * n + 2] + newPixel[2 * m * 3 * width + 3 * n + 3 * width + 2]) / 2)
newPixelaveH.extend(tempPixel)

newfile = open('balls_inversed.ppm', "w")

newfile.write("P3\n")
newfile.write(str(256) + " " + str(256) + "\n")
newfile.write("255\n")

for i in range(height):
    for j in range(width):
        newfile.write(str(newPixelaveH[3 * i * width + 3 * j]) + " ")
        newfile.write(str(newPixelaveH[3 * i * width + 3 * j + 1]) + " ")
        newfile.write(str(newPixelaveH[3 * i * width + 3 * j + 2]) + " ")
    newfile.write("\n")

newfile.close()
