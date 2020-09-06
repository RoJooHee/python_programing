#2개 이상의 행렬 더하는 코드
#행렬 크기 일정치 않음

def matrix_add(x, y):
    result=[[sum(sc) for sc in zip(*vec)] for vec in zip(x, y)]
    #x,y에서 같은 인덱스들 뽑아 vec으로 묶고, vec에서 같은 인덱스들 뽑은 sc들을 합함
    print(result)

matrix_x=[[2,5], [2,1], [3,5]]
matrix_y=[[3,4], [5,6], [7,8]]
matrix_add(matrix_x, matrix_y)
