aocList = open(r"C:\Users\Neal\Desktop\Advent of Code\day3Data.txt")

try:
    aocData = aocList.readlines()
finally:
    aocList.close()
    
treeCount = 0
xPos = 0
for line in aocData:
    tile = line[xPos%31]
    if tile == '#':
        treeCount +=1
    xPos += 3


print(treeCount)