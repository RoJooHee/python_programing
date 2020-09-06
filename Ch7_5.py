#표준입력으로 첫번째줄 문자열 여러개=키, 두번째 줄 숫자 여러개=값 입력해서 딕셔너리 생성
#생성된 딕셔너리에서 키가 'delta' 또는 값이 '30'인 키-값 쌍은 삭제하고 출력

a=input("문자열 여러개 입력 : ").split()
b=input("숫자 여러개 입력 : ").split()

for i in range(len(b)):
    b[i]=int(b[i]) #딕셔너리에서 ''가 없는 int 형이기에 형변환함

dict={}
dict.update(zip(a,b)) #빈 딕셔너리 dict에 a,b 리스트를 a[0]b[0], a[1]b[1].. 을 쌍으로 딕셔너리로 저장해 합침

for key, value in dict.items(): #dict의 key,value를 for문을 돌며 조건 검색
    if key=='delta':
        dict={key: value for key, value in dict.items() if key != 'delta'} #key가 delta인 것 제외하고 dict생성
    elif value==30:
        dict={key: value for key, value in dict.items() if value != 30}  #value가 30인 것 제외하고 dict생성

print(dict) #삭제 후 조건에 맞는 딕셔너리 dict 출력


#위의 표현식을 쓰지 않고 임의로 딕셔너리 크기가 바뀌지 않게 쌍을 추가해도 작동이 잘 되던데, 이렇게 해도 괜찮은건가요?
#for key, value in dict.items(): #dict의 key,value를 for문을 돌며 조건 검색
#    if key=='delta':
#        del dict['delta']
#        dict.update({1:''}) #딕셔너리 크기가 바뀌지 않도록 삭제 후 키가 문자열 아닌 숫자 1인 쌍을 만들어줌
#
#    elif value==30:
#        del dict[key]
#        dict.update({2:''}) #딕셔너리 크기가 바뀌지 않도록 삭제 후 키가 문자열 아닌 숫자 2인 쌍을 만들어줌
#del dict[1] #임의로 만든 쌍은 다시 삭제해줌
#del dict[2] # 위와 같음
#print(dict)
