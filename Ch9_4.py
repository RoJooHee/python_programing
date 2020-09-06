#2개 이상의 벡터 빼는 코드

def vector_sub(vec, *args):
    #A-B-C-D=A-(B+C+D)이므로 먼저 뒤의 벡터들(*agrs)을 다 합함
    total=[sum(sc) for sc in zip(*args)] #뺄 벡터들을 합함

    #A-(total)=A+(-total)이므로, total값들을 -1과 곱해줌
    subnum=[sc*-1 for sc in total]

    #가장처음 벡터 vec과 합해서 -1과 곱한 뺄셈할 벡터 subnum을 같은 인덱스끼리 뽑아서 합함
    result=[sum(sc) for sc in zip(vec, subnum)]
    print(result)

vector_sub([1,3], [2,4])
vector_sub([1,5], [10,4], [4,7])
vector_sub([10,9,8], [1,2,3], [3,4,5], [1,1,1])
