import sys

with open(str(sys.argv[1])) as ifile:
    inputs = ifile.readlines()


def boot(inputs):
    accumulator = 0
    instructionIter = 0
    instructionsCompleted =[]
    while True:
        if instructionIter in instructionsCompleted:
            return "loop"
        if instructionIter >= len(inputs):
            return accumulator

        if inputs[instructionIter].find("nop") == 0:
            instructionsCompleted.append(instructionIter)
            instructionIter += 1
            continue

        if inputs[instructionIter].find("jmp") == 0:
            instructionsCompleted.append(instructionIter)
            instructionIter += int(inputs[instructionIter][4:])
            continue

        if inputs[instructionIter].find("acc") == 0:
            instructionsCompleted.append(instructionIter)
            accumulator += int(inputs[instructionIter][4:])
            instructionIter += 1
            continue


for i,line in enumerate(inputs):
    copy = inputs.copy()
    if line.find("nop") == 0:
        copy[i] = line.replace("nop", "jmp")
        if boot(copy) == "loop":
            copy[i] = line
            continue
        print(boot(copy))
        break
    if line.find("jmp") == 0:
        copy[i] = line.replace("jmp", "nop")
        if boot(copy) == "loop":
            copy[i] == line
            continue
        print(boot(copy))
        break

