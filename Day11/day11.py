import sys

with open(sys.argv[1], "r") as ifile:
    inp = ifile.read().split("\n")
    inp.pop()


def changeSeats(new, old):
    for i, line in enumerate(old):
        new.append("")
        for j, space in enumerate(line):
            up = i-1
            down = i+1
            left = j-1
            right = j+1

            if space == "L":
                if left == -1:
                    nw, w, sw = True, True, True
                if up == -1:
                    nw, n, ne = True, True, True
                if down == len(old):
                    sw, s, se = True, True, True
                if right == len(line):
                    ne, e, se = True, True, True
                if 'nw' not in locals():
                    nw = old[up][left] == "L" or old[up][left] == "."
                if 'n' not in locals():
                    n = old[up][i] == "L" or old[up][i] == "."
                if 'ne' not in locals():
                    ne = old[up][right] == "L" or old[up][right] == "."
                if 'e' not in locals():
                    e = old[i][right] == "L" or old[i][right] == "."
                if 'se' not in locals():
                    se = old[down][right] == "L" or old[i][right] == "." 
                if 's' not in locals():
                    s = old[down][i] == "L" or old[down][i] == "."
                if 'sw' not in locals():
                    sw = old[down][left] == "L" or old[down][left] == "."
                if 'w' not in locals():
                    w = old[i][left] == "L" or old[i][left] == "." 

                if nw and n and ne and e and se and s and sw and w:
                    new[i] += "#"
                else:
                    new[i] += "L"

            if space == ".":
                new[i] += "."

            if space == "#":
                if left == -1:
                    nw, w, sw = 0,0,0
                if up == -1:
                    nw, n, ne = 0,0,0
                if down == len(old):
                    sw, s, se = 0,0,0
                if right == len(line):
                    ne, e, se = 0,0,0
                if 'nw' not in locals():
                    nw = 1 if old[up][left] == "#" else 0
                if 'n' not in locals():
                    n = 1 if old[up][i] == "#" else 0
                if 'ne' not in locals():
                    ne = 1 if old[up][right] == "#" else 0
                if 'e' not in locals():
                    e = 1 if old[i][right] == "#" else 0
                if 'se' not in locals():
                    se = 1 if old[down][right] == "#" else 0
                if 's' not in locals():
                    s = 1 if old[down][i] == "#" else 0
                if 'sw' not in locals():
                    sw = 1 if old[down][left] == "#" else 0
                if 'w' not in locals():
                    w = 1 if old[i][left] == "#" else 0
                if nw + n + ne + e + se + s + sw + w >= 4:
                    new[i]+="L"
                else:
                    new[i]+="#"

            if 'nw' in locals():
                del nw
            if 'n' in locals():
                del n
            if 'ne' in locals():
                del ne
            if 'e' in locals():
                del e
            if 'se' in locals():
                del se
            if 's' in locals():
                del s
            if 'sw' in locals():
                del sw
            if 'w' in locals():
                del w
    
    for i,k in enumerate(old):
        for j,l in enumerate(k):
            if old[i][j] != new[i][j]:
                return changeSeats([], new)
    
    return new

#print(inp)
print(changeSeats([],inp))
count = 0
for line in changeSeats([], inp):
    count+=line.count("#")
print(count)
