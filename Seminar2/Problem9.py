
def testSight(matrix,row,column) :
    rows = len(matrix)
    return len([True for el in range(0,row) if matrix[row][column] <= matrix[el][column]]) != 0 

def notSeeingSpectators(seats) : 
    rows = len(seats)
    columns = len(seats[0])
    return [(row,column) for row in range(0,rows) for column in range(0,columns) if testSight(seats,row,column)]

var = [[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 7, 2],
[5, 5, 2, 5, 6, 4],
[6, 6, 7, 6, 7, 5]]

print(notSeeingSpectators(var))