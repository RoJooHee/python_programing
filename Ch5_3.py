#피보나치 f(n)=f(n-1)+f(n-2)
num=int(input("피보나치 계산을 원하는 수를 입력하세요: "))
while num>50 or num<=2 : num=int(input("2<n<=50 사이의 수로 입력하세요: "))

def f(x):
    if x<2 : return x
    else : return f(x-1)+f(x-2)

a=f(num)
print(a)
