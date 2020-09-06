#2개이상 행렬 곱
#입력되는 행렬크기 일정x

def matrix_mul(x, y):
    result=[[sum(sc*sc2 for sc, sc2 in zip(vec, vec2)) for vec2 in zip(y)] for vec in x ]
    #1. x행렬의 각 벡터들 vec / 2. y행렬에서 각 벡터의 같은 인덱스들 vec2
    #3. vec과 vec2의 같은 인덱스들끼리 곱하고 그 값들을 합함
    print(result)

matrix_x=[[1,2,3], [4,5,6]]
matrix_y=[[1,2], [3,4], [5,6]]
matrix_mul(matrix_x, matrix_y)
