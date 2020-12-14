import sys

with open(str(sys.argv[1]),"r") as ifile:
    bspList = ifile.readlines()

def getRow(bsp):
    #Cut down to first 7 characters of the string
    rowDirections = bsp[:7]
    
    #List of every row
    rows = []
    for i in range(0,128):
        rows.append(i)
    
    #find correct row from directions
    for d in rowDirections:
        if d == "F": #lower half
            rows = rows[:int((len(rows))/2)]
        elif d == "B": #upper half
            rows = rows[int((len(rows))/2):]

    return rows[0]

def getColumn(bsp):
    #Cut to final 3 characters
    colDirections = bsp[-4:]
    #list of each column
    cols = []
    for i in range(0,8):
        cols.append(i);

    #find correct col from directions
    for d in colDirections:
        if d == "L":
            cols = cols[:int(len(cols)/2)]
        elif d == "R":
            cols = cols[int(len(cols)/2):]

    return cols[0]

maxseatid = 0

seatidList = []

for bsp in bspList:
    row = getRow(bsp)
    col = getColumn(bsp)
    seatid = (row * 8) + col
    seatidList.append(seatid)
    if seatid > maxseatid:
        maxseatid = seatid

seatidList.sort()
myseatid = 0

for i in range(0, len(seatidList)-1):
    if seatidList[i+1] - seatidList[i] == 2:
        myseatid = seatidList[i]+1

print(maxseatid)
print(myseatid)
