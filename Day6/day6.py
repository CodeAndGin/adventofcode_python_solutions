import sys

with open(str(sys.argv[1]),"r") as ifile:
    ins = ifile.read()

#split into groups

groups = ins.split("\n\n")

#split into people

#for i in range (0, len(groups)):
#    groups[i] = groups[i].split("\n")

groups = [group.split("\n") for group in groups]
groups[-1].pop()


count = 0
allcount = 0

for group in groups:
    answered = []
    allanswered = []
    for person in group:

        for answer in person:

            if answer not in answered:
                answered.append(answer)

    answered.sort()
    allanswered = answered.copy()

    for answer in answered:

        for person in group:

            if answer not in person and answer in allanswered:
                allanswered.remove(answer)

    count+=len(answered) #part1
    allcount += len(allanswered) #part2
print(allcount)
