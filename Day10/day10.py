import sys

with open(str(sys.argv[1]),"r") as ifile:
    inputs = ifile.readlines()
    for i,k in enumerate(inputs):
        inputs[i] = int(k)


sortedinputs = inputs.copy()
sortedinputs.sort()

OUTPUT = 0
DEVICE = sortedinputs[-1]+3

totdiff = 0
totones = 0
totthrees = 1
if sortedinputs[0] == 1:
    totones+=1
elif sortedinputs[0] == 3:
    totthrees+=1

for i,k in enumerate(sortedinputs):
    if i < len(sortedinputs)-1:
        diff = sortedinputs[i+1]-k
        totdiff += diff
        if diff == 1:
            totones+=1
        elif diff == 3:
            totthrees+=1
totdiff+=3
print(totones*totthrees) #part 1 answer

#Part 2 start

sortedinputs.append(OUTPUT)
sortedinputs.sort()
sortedinputs.append(DEVICE)

#full disclosure, hod to find some solutions to figure this out
#Original looked almost exactly like this just without the memoization
#That was my next go to idea, but checked the reddit for hints and that confirmed it
#Then redid my algorithm memoized
#The only thing I dont know if I would have done myself is use a Dict, that defo saved
#a few ines of checks

def buildArrangements(start, array, store={}):
    if start>=array[-1]:
        return 1
    if start not in array:
        return 0
    elif start not in store:
        store[start] = buildArrangements(start+3,array, store) + buildArrangements(start+2, array,store) + buildArrangements(start+1,array,store)
    return store[start]


print(buildArrangements(sortedinputs[0], sortedinputs))
