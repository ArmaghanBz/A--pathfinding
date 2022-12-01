matrix = [['','A','',''],
          ['','','',''],
          ['','','',''],
          ['','','','B']
          ]

startingPoint = ()
goalPoint = ()
listsOfneighbour = []

for i, j in enumerate(matrix):
    if 'A' in j:
        startingPoint = (i, j.index('A'))

print("Starting Point", startingPoint)

for i, j in enumerate(matrix):
    if 'B' in j:
        goalPoint = (i, j.index('B'))
print("Ending point", goalPoint)

def findNeighbour(cell):
    row = startingPoint[0]
    col = startingPoint[1]
    if row - 1 >= 0:
        listsOfneighbour.append((row-1,col))
    if col - 1 >= 0:
        listsOfneighbour.append((row,col-1))
    if row + 1 <= 3:
        listsOfneighbour.append((row+1,col))
    if col + 1 <= 3:
        listsOfneighbour.append((row,col+1))
    return listsOfneighbour

def heuristicValue(set1, set2):
    return abs(set1[0]-set2[0])+ abs(set1[1]-set2[1])

print("\n")
#main working
value = 'A'
g_x = 0
while value != 'B':
    neighbours = findNeighbour(startingPoint)
    h_x = []
    for each in neighbours:
        h_x.append(heuristicValue(each,goalPoint))
    min_distant = h_x.index(min(h_x))
    startingPoint = neighbours[min_distant]
    print("Next Point =>", startingPoint)
    value = matrix[startingPoint[0]][startingPoint[1]]
    g_x = g_x + 1
print("number of steps taken = ",g_x)

