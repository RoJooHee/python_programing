dan=int(input("1-9몇단? :"))
while(dan<=9 and dan>=1):
    print(dan, "단 출력")
    for i in range(1,10,1):
        print(dan, "*", i, "=", dan*i)
    dan=int(input("단 다시 입력: "))
else:
    if dan==0: print("종료")
