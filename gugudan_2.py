print("구구단 몇단?: ")
x=1
while(x is not 0):
    x=int(input())
    if x==0: break
    if not(1<=x<=9):
        print("잘못입력. 1-9입력")
        continue
    else:
        print("구구단",x,"단 계산")
        for i in range(1,10):
            print(x,"x",i,"=",x*i)
        print("구구단 몇단 계산?: ")
print("종료")
