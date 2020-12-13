import sys

with open(str(sys.argv[1]), "r") as ifile:
    passwords = ifile.readlines()

count = 0

for pas in passwords:
    sep = pas.split(' ')
    #sep[0] is nums
    #sep[1] is chars
    #sep[2] is pass
    nums = sep[0].split('-')
    lo = int(nums[0])
    hi = int(nums[1])
    #if sep[2].count(sep[1][0]) <= hi and sep[2].count(sep[1][0]) >= lo:
    #    count+=1
    if (sep[2][lo-1] == sep[1][0]) != (sep[2][hi-1] == sep[1][0]):
        count+=1


print(count)
