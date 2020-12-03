aocList = open(r"C:\Users\Neal\Desktop\Advent of Code\day2Data.txt")

try:
    aocData = aocList.readlines()
finally:
    aocList.close()
    #print(aocData)

validPass = 0

for line in aocData:
    nonpassword, password = line.split(": ")
    limits, target = nonpassword.split(" ")
    firstTarget, secondTarget = limits.split("-")
    firstTarget = int(firstTarget)
    secondTarget = int(secondTarget)
    firstLetter = password[firstTarget-1]
    secondLetter = password[secondTarget-1]
    if (firstLetter == target) is not (secondLetter == target):
        validPass += 1


print(validPass)
