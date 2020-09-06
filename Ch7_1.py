#1에서 100까지 숫자 출력
#5의 배수는 Fizz / 7의 배수는 Buzz 출력 / 5과 7의 공배수는 FizzBuzz 출력

for i in range(1,101,1):
    if (i%5==0 and i%7==0) : print('FizzBuzz')
    elif (i%5==0) : print('Fizz')
    elif (i%7==0) : print('Buzz')
    else : print(i) #해당되지 않는경우 i에 해당하는 숫자 그대로 출력
