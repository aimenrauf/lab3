def add(matrix1, matrix2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range (3):
        for j in range (3):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,8,7],[6,5,4],[3,2,1]]
resultant = add(matrix1,matrix2)
print("Matrix 1: ")
for row in matrix1:
    print (row)
print("Matrix 2: ")
for row in matrix2:
    print(row)
print("Resultant Matrix: ")
for row in resultant:
    print(row)
