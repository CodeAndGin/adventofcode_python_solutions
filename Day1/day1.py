import sys


with open(str(sys.argv[1]), "r") as ifile:
    numbers = ifile.readlines()

a = 0
b = 0

for i in numbers:
    for j in numbers:
        for k in numbers:
            if int(i)+int(j)+int(k)==2020:
                print(int(i)*int(j)*int(k))
