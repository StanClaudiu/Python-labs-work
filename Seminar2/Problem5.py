def replaceElements(matrix) :
    lines = len(matrix)
    return [[ matrix[line][column] if line < column  else 0 for column in range(0,lines)] for line in range(0,lines)]

print(replaceElements([[1 for x in range(0,3)] for x in range(0,3)]))

