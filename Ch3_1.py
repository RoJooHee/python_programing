#숫자의 개수 num개
num=int(input("숫자를 입력하세요 : "))
while num>100 or num<1 :
    print("1~100 사이의 숫자로 다시 입력하세요 : ")
    num=int(input())

#숫자 공백없이 입력
numbers=input(("합하고 싶은 1의자리 숫자들을 입력하세요: "))
sum=0

#반복적으로 numbers 숫자 중 n개를 합하기
for i in range(num) :
    sum+=int(numbers[i])

print(sum)
