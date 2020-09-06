#테스트 케이스의 개수
T = int(input("케이스 개수를 입력하세요 : "))
while T>1000 or T<1 :
    T = int(input("1 <= T <= 1000 로 케이스 개수를 다시 입력하세요: "))


for i in range(T) : #range(t)= 0~t-1번 반복
    out_char = ""

    #테스트 케이스 반복횟수 R, 문자열 S를 공백 기준으로 나눠받기
    R, S = input("'반복횟수 문자열'을 입력하세요 : ").split()
    while (int(R)>8 or int(R)<1) or (len(S)>20 or len(S)<1) :
        R,S = input("반복횟수( 1<=R<=8 ), 문자열길이( 1<=length<=20 ) 다시입력하세요 : ").split()

    #S문자열을 J라는 변수로 한글자씩 받아오며 R번씩 반복해 out_char에 저장
    for J in S :
        out_char += J * int(R)

    print(out_char)
