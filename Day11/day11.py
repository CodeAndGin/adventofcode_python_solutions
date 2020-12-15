import sys

with open(sys.argv[1], "r") as ifile:
    inp = ifile.read().split("\n")
    inp.pop()

test = ["L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL"]

def changeSeats(old):
    new = []
    for i, line in enumerate(old):
        new.append("")
        for j, space in enumerate(line):
            if space == "L":
                changes = True
                for a in range(i-1,i+2):
                    for b in range(j-1,j+2):
                        if b==j and i==a: continue
                        if a < 0: continue
                        if b < 0: continue
                        if a > len(old) - 1: continue
                        if b > len(line) - 1: continue

                        if old[a][b] == "#":
                            changes = False

                if changes:
                    new[i]+="#"
                else:
                    new[i]+="L"

            if space == ".":
                new[i] += "."

            if space == "#":
                count = 0
                for a in range (i-1,i+2):
                    for b in range (j-1,j+2):
                        if b==j and a==i: continue
                        if a<0: continue
                        if b<0: continue
                        if a>len(old)-1: continue
                        if b>len(line)-1: continue

                        if old[a][b] == "#":
                            count+=1
                if count >= 4:
                    new[i]+="L"
                else:
                    new[i]+="#"
                

    
    #for i,k in enumerate(old):
        #for j,l in enumerate(k):
            #if old[i][j] != new[i][j]:
                #return changeSeats(new)
    
    return new

def changeSeatsLineOfSight(old):
    print(old)
    new = []
    for i, line in enumerate(old):
        new.append("")
        #print(old[i])
        #print(len(line))
        for j, space in enumerate(line):

            if space == ".":
                new[i]+="."
                continue

            seen = []

            for a in range (i-1,i+2):
                for b in range (j-1,j+2):
                    if b==j and a==i: continue
                    if a<0: continue
                    if b<0: continue
                    if a>len(old)-1: continue
                    if b>len(old[i])-1: continue
                    x = a
                    y = b
                    #print(a, b, len(old),len(line))
                    see = old[x][y]
                    while see == ".":
                        if x-1 < 0: break
                        if x+1 >= len(old): break
                        if y-1 < 0: break
                        if y+1 >= len(line): break
                        if a == i-1: x-=1
                        if b == j-1: y-=1
                        if a == i+1: x+=1
                        if b == j+1: y+=1
                        if a == i: x = a
                        if b == j: y = b 
                        see = old[x][y] #need safeguards
                    seen.append(see)
            #print(seen)
            if space == "L" and seen.count("#") == 0:
                new[i] += "#"
            elif space == "#" and seen.count("#") >=5:
                new[i] += "L"
            else:
                new[i] += "#"

    if old == new:
        return new
    else:
        return changeSeatsLineOfSight(new)



prev = inp.copy()

new = []
count = 0
new = changeSeatsLineOfSight(test)
for i in new:
    count+= i.count("#")
print (count)
while True:
    new = changeSeats(prev).copy()
    if new == prev:
        break
    #for i in new:
        #print(i)
    prev = new.copy()


#new = changeSeats(inp)
#for i in new:
#    print(i)

count = 0
for i in new:
    count+=i.count("#")

print(count)

