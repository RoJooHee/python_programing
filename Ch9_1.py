#표준입력 10<=N<=50 -> N! 출력 1000단위마다 , 넣기
#람다함수, reduce()함수 사용
# 20 -> 2,432,902,008,176,640,000

N=int(input("팩토리얼 계산 원하는 수 입력: "))
while(N<10 or N>50):
    N=int(input("팩토리얼 계산 원하는 수 다시 입력: ")) #N 범위 조건에 맞게 입력받음

list=[]
for i in range(N):
    list.append(i+1) #list에 1~N 까지 차례로 넣음

from functools import reduce

fac=reduce(lambda x, y: x*y, list) #reduce, 람다함수 이용해 리스트 값 차례대로 곱함

print("{:9,}".format(fac)) #값 형식으로 출력함
