def mul(*values):
    #곱셈할 변수와 값을 선언한다.
    multiply=1
    #values에 있는 값들을 계속 곱해나간다.
    for i in values:
        multiply=multiply*i
    return multiply

print(mul(5,7,9,10))
