n=int(input("구하고 싶은 n까지의 누가합계를 입력하세요. n="))

#n 숫자 조건에 맞지 않으면 재입력
while n>10000 or n<1:
    n=int(input("1~10000사이의 숫자로 다시 입력하세요: "))

#sum에 for문을 통해 1~n의 누적합을 저장할 수 있게 함.
#range(n)은 0~n-1이어서 i+1을 합해주도록 함
sum=0
for i in range(n):
    sum=sum+(i+1)

print(sum)
