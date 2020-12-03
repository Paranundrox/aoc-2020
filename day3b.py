aocList = open(r"C:\Users\Neal\Desktop\Advent of Code\day3Data.txt")

try:
    aocData = aocList.readlines()
finally:
    aocList.close()
    
xSlope = [1, 3, 5, 7, 1]
ySlope = [1, 1, 1, 1, 2]
totalCount = [] 

for j in range(0, len(xSlope)):
    treeCount = 0
    xPos = 0
    for i in range(0, len(aocData), ySlope[j]):
        
        line = aocData[i]
        tile = line[xPos%31]
        if tile == '#':
            treeCount +=1
        xPos += xSlope[j]
    totalCount.append(treeCount)

print(totalCount)
print(totalCount[0]* totalCount[1]* totalCount[2]* totalCount[3]* totalCount[4])