import sys

with open(str(sys.argv[1]),"r") as ifile:
    passes = ifile.read()

#seperate passes
passes = passes.split("\n\n")

parsedpasses = []

for pas in passes:
    newpass = []
    newlinesplit = pas.split("\n")
    for line in newlinesplit:
        spacesplit = line.split(" ")
        for datum in spacesplit:
            newpass.append(datum)
    parsedpasses.append(newpass)

for i in range(0, len(parsedpasses)):
    for j in range (0, len(parsedpasses[i])):
        parsedpasses[i][j] = parsedpasses[i][j].split(":")
parsedpasses[-1].pop(-1)
dictpaslist = []

for i in range(0,len(parsedpasses)):
    newdict = {}
    for j in range(0, len(parsedpasses[i])):
        newdict[parsedpasses[i][j][0]] = parsedpasses[i][j][1]
    dictpaslist.append(newdict)


count = 0
keys=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
for pas in dictpaslist:
    keycount = 0
    for key in keys:
        if key in pas:
            keycount+=1
    if keycount==7:
        count+=1

count = 0
for pas in dictpaslist:
    keycount = 0
    for key in keys:
        if key in pas:
            if key == "byr":
                if int(pas[key])>=1920 and int(pas[key])<=2002:
                    keycount+=1
            if key == "iyr":
                if int(pas[key])>=2010 and int(pas[key])<=2020:
                    keycount+=1
            if key == "eyr":
                if int(pas[key])>=2020 and int(pas[key])<=2030:
                    keycount+=1
            if key == "hgt":
                if pas[key].find("cm") != -1:
                    value = pas[key]
                    value = int(value[:-2])
                    if value>=150 and value<=193:
                        keycount+=1
                elif pas[key].find("in") != -1:
                    value = int(pas[key][:-2])
                    if value>=59 and value<=76:
                        keycount+=1
            if key == "hcl":
                if pas[key][0] == "#" and len(pas[key]) == 7:
                    value = pas[key][1:]
                    valids = "0123456789abcdef"
                    valid = True
                    for char in value:
                        if char not in valids:
                            valid = False
                    if valid:
                        keycount+=1
            if key == "ecl":
                for col in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    if pas[key]==col:
                        keycount+=1
                        break
            if key == "pid":
                if len(pas[key]) == 9 and pas[key].isnumeric():
                    keycount+=1
    if keycount==7:
        count+=1
print (count)
    
