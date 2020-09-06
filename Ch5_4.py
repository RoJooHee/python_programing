N=int(input("팩토리얼을 원하는 수를 입력하세요: "))
while N>1000000 and num<9 : N=int(input("9<=N<1000000 사이의 수로 입력하세요: "))

#for문 이용
#def fac(n):
#    global a
#    for i in range(n, 0, -1):
#        a=a*i
#    return a
#
#a=1

#재귀함수 이용
def fac(n):
    if n==1 : return 1
    else : return n*fac(n-1)

f=fac(N)
#함수에서 return된 값이 저장된 f를 문자들의 리스트로 만들어 listf로 저장한다
list_f=list(str(f))

#만약 팩토리얼값 리스트의 맨 마지막 부분이 0이면, 그 부분을 계속하여 삭제한다.
while list_f[-1]=='0' :
    del list_f[-1]

#맨 마지막이 0이 아닌 listf를 뒤에서 5자리만 출력하게 하여 value에 저장한다.
value=list_f[-5:]
#value에 있는 값은 리스트 형태이므로 다시 문자열형태로 바꾸어 출력한다.
print(''.join(value))
