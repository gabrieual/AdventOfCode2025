def adjacents(matrix:[[str]], i:int, j:int) -> int:
    pos = [-1,0,1]
    adjacents = -1

    for m in pos:
        for n in pos:
            if (i+m < 0) | (i+m >= len(matrix)) | (j+n < 0) | (j+n >= len(matrix[i])):
                continue
            if matrix[i+m][j+n] == "@":
                adjacents += 1

    return adjacents

matrix = []

with open("day4_input") as file:
    for line in file:
        line = line[:-1]
        matrix.append(list(line))

answer = 0
removed = -1

while(removed):
    removed = 0
    for i in range(len(matrix)):
        for j in range(len(line)):
            if (matrix[i][j] == "@") and (adjacents(matrix, i, j) < 4):
                removed += 1
                matrix[i][j] = '.'
    
    answer += removed 

print(answer)