

with open("pos1colors.ppm", 'r') as fn:
    file_object = fn.readlines()

fn.close()
wh = file_object[1].split()
originalwidth = int(wh[0])
originalheight = int(wh[1])
L = file_object[3:]
# start with the fourth line, first three lines are useless for the operation below


print(L[10:])