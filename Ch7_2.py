#표준입력으로 정수 2개 입력 (1~20, 10~30. 첫째<둘째)
#첫번째 정수로부터 두번쨰 정수까지를 지수로하는 2의 거듭제곱 리스트 출력
#리스트의 두번쨰, 뒤에서 두번쨰 요소는 빼고 출력
#출력결과는 리스트형태
a, b=map(int, input("숫자 두개를 공백 기준으로 입력하세요 : ").split())
a=int(a)
b=int(b)

while a>20 or a<1 or b>30 or b<10 or a>=b :
    a, b=input("숫자 두개를 공백 기준으로 입력하세요 : ").split()
    a=int(a)
    b=int(b)

num=[]
for i in range(a, b+1, 1):
    num.append(2**i) #2의 거듭제곱 리스트 num 생성

del num[1] #리스트의 두번쨰 요소를 뺌
del num[b-a-2] #리스트의 뒤에서 두번째 요소를 뺌
print(num) #두개 요소를 뺀 나머지 리스트를 출력
