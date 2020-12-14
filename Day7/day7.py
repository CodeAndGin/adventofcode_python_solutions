import sys

with open(str(sys.argv[1])) as ifile:
    inputs = ifile.readlines()

count = 0
parents = []

for line in inputs:
    if line.rfind("shiny gold") > 0:
        count+=1
        parent = line[:line.find(" ", line.find(" ")+1)]
        parents.append(parent)

dupecheck = parents.copy()

def findparentsrecursively(parents):
    newparents = []
    c = 0
    for p in parents:
        for line in inputs:
            if line.rfind(p) > 0:
                newparent = line[:line.find(" ", line.find(" ")+1)]
                if newparent not in dupecheck:
                    c+=1
                    dupecheck.append(newparent)
                    newparents.append(newparent)
    if len(newparents) > 0:
        return c+findparentsrecursively(newparents)
    else:
        return 0

count += findparentsrecursively(parents)
print(count)

#end of part 1
#part 2

count = 0
children = []

for line in inputs:
    if line.find("shiny gold") == 0:
        s = line[line.find("bags contain")+13:]
        s = s.split(", ") #X adj col bag(s)(.)
        for i, a in enumerate(s):
            s[i] = a[:a.rfind(" ")]
            children.append([s[i][2:], int(s[i][0])])


#count = children[i][1] + children[i][1] * childrenof(children[i][0]) for each i

def childrenof(child):
    c = 0
    newchildren = []

    for line in inputs:
        if line.find("no other") > 0:
            pass
        elif line.find(child) == 0:
            s = line[line.find("bags contain")+13:]
            s = s.split(", ")
            for i, a in enumerate(s):
                s[i] = a[:a.rfind(" ")]
                newchildren.append([s[i][2:], int(s[i][0])])
    #print(newchildren)
    if len(newchildren) > 0:
        for i,ch in enumerate(newchildren):
            c += ch[1] + ch[1]*childrenof(ch[0])
    return c

for i, ch in enumerate(children):
    count += ch[1] + ch[1] * childrenof(ch[0])

print(count)
