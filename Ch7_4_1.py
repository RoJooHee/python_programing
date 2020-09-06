col, row = map(int, input("입력: ").split())

matrix = []
for i in range (row):
    matrix.append(list(input("리스트: ")))

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()


for i in range(row):
    for j in range(col):
        if matrix[i][j] == "*":
            print(matrix[i][j], sep='', end='')
        else:
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue
                    elif matrix[x][y] == "*":
                        count += 1
            print(count, sep='', end='')

    print()




#matrix=[]
#for j in range(row):
#    matrix_1=[]
#    for I in range(col):
#        matrix_1.append(list(input())) #여기서 enter안치고 가로줄 각각으로 인식되게 입력하는방법?
#    matrix.append(matrix_1)
