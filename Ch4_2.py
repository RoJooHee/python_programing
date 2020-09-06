year=int(input("윤년 계산을 원하는 연도를 입력하세요: "))

#year 숫자 조건에 맞지 않으면 재입력
while year>4000 or year<1:
    year=int(input("연도는 1~4000으로 다시 입력하세요: "))

#4의 배수이면서 100의 배수가 아니고, 400의 배수는 해당할 때 1 출력
if (year%4==0 and year%100!=0) or year%400==0: print("1")
else: print("0")
