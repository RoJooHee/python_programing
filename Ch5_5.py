def flatten(data):
    #리스트를 만들기 위해 빈 리스트 선언
    result=[]
    #data 리스트에 들어있는 각 값들로 for문을 돌린다.
    for element in data:
        #리스트 안에 있던 값이 리스트라면 함수 재귀호출하여 리스트에서 벗어나도록 한다.
        #각각 하나의 숫자인 element를 리스트로 만들어 result리스트와 합친다.
        if type(element)==list: result=result+flatten(element)
        else: result=result+[element]
    return result

example=[[1,2,3], [4,[5,6]], 7, [8,9]]
print(example+3)
print("원본: ", example)
print("변환: ", flatten(example))
