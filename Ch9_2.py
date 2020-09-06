#하나의 스칼라 값을 벡터에 곱하기.
#입력되는 벡터크기는 일정하지 않음

def scalar_vector_product(sc, vec):
    result=[sc*t for t in vec] #스칼라에 벡터를 차례대로 곱해서 리스트에 넣음
    print(result)

scalar_v=5
vector_list=[1,3,5,7,11,13]
scalar_vector_product(scalar_v, vector_list)
