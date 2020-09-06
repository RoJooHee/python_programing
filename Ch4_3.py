a, b, c=input("숫자 3개를 공백기준으로 입력하세요: ").split()

#공백 기준으로 나뉜 a,b,c를 계산을 위해 int형으로 바꿔줌
a=int(a)
b=int(b)
c=int(c)

#a,b,c 숫자 조건에 맞지 않으면 재입력
while (a or b or c)>100 or (a or b or c)<1:
    a, b, c=int(input("1~100 사이로 다시 입력하세요: ").split())

#숫자 3개를 t라는 리스트로 패킹하고, 숫자 비교를 위해 오름차순으로 정리함
t=[a,b,c]
t=sorted(t)

#두번쨰로 큰 숫자이므로 리스트의 인덱스 1번째 숫자를 출력함
print(t[1])
