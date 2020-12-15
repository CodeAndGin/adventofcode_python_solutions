import sys

with open(str(sys.argv[1]), "r") as ifile:
    inputs = ifile.readlines()

for i,k in enumerate(inputs):
    inputs[i] = int(k)

invalid = 0

for i in range(25, len(inputs)):
    valid = False
    for j in range(i-25,i):
        for k in range(i-25,i):
            if j==k:
                continue
            if inputs[j] + inputs[k] == inputs[i]:
                valid = True
    if valid == False:
        invalid = inputs[i]
        print(invalid, i)
        break

trueI,trueJ = -1,-1

for i,k in enumerate(inputs):
    j = i+1
    tot = inputs[i]
    while True:
        #print(i, j, tot<=invalid, tot, invalid)
        if tot < invalid:
            tot += inputs[j]
            j+=1
        elif tot == invalid:
            #print(i, j, tot<=invalid, tot, invalid)
            trueI = i
            trueJ = j
            break
        else:
            #print(i, j, tot<=invalid, tot, invalid)
            break
    if trueI >= 0:
        break

a = inputs.copy()
a = a[trueI:trueJ+1]
a.sort()
print(a[0]+a[-1])


