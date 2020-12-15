import sys

with open(str(sys.argv[1]),"r") as ifile:
    inputs = ifile.readlines()
    for i,k in enumerate(inputs):
        inputs[i] = int(k)

print(inputs)
