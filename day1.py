aocList = open(r"C:\Users\Neal\Desktop\Advent of Code\day1Data.txt")
i = 0
try:
    aocData = aocList.readlines()
    for line in aocData:
        aocData[i] = int(line)
        i += 1
finally:
    aocList.close()
    #print(aocData)

sumsList = []

for firstValue in aocData:
    for secondValue in aocData:
        for thirdValue in aocData:
            testSum = firstValue + secondValue + thirdValue
            if testSum == 2020:
                finalVal1 = firstValue
                finalVal2 = secondValue
                finalVal3 = thirdValue

print(finalVal1 + finalVal2 + finalVal3)
print(finalVal1)
print(finalVal2)
print(finalVal3)
print(finalVal1*finalVal2*finalVal3)


