# def replaceElements(matrix) :
#     lines = len(matrix)
#     return [[ if line > column matrix[line][column] else 0 for column in range(0,lines)] for line in range(0,lines)]

print([if ch > 0  ch else -1  for ch in [-1,-2,1,2] ])
