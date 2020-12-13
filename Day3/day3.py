import sys

with open(str(sys.argv[1]),"r") as ifile:
    rows = ifile.readlines()

count = 0

right = 0

def replace(string, index, char):
    new = ""
    for i in range (0, len(string)):
        if i == index:
            new += char
            continue
        new += string[i]
    return new

down = 0;

for row in rows:
    if down%2 == 1:
        print(row)
        down+=1
        continue

    if row[right] == '#':
        row = replace(row, right, 'X')
        count += 1
    else:
        row = replace(row, right, 'O')
    right+=5
    right%=len(row)-1
    down+=0
    print(row)

print(count)

