#테스트 케이스의 개수
T = int(input("케이스 개수를 입력하세요 : "))
while T>1000 or T<1 :
    T = int(input("1 <= T <= 1000 로 케이스 개수를 다시 입력하세요: "))

#S문자열을 J라는 변수로 한글자씩 받아오며 R번씩 반복해 out_char에 저장
for J in 'abcde' :
    out_char += J * int(R)

#2차원리스트
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])

c.sort() -> print(c) = 정렬됨
c=c.sort() -> print(c) = none
c=sorted(c) -> print(c) = 정렬됨

#maping함수와 여러개숫자 int로 바꾸기
a, b, c=input("숫자 3개를 공백기준으로 입력하세요: ").split()
a=int(a) ;; b=int(b) ;; c=int(c)
#or
a, b, c=map(int, input("숫자 3개를 공백기준으로 입력하세요: ").split())
#or 숫자개수 모를때
b=input("숫자 여러개 입력 : ").split()
for i in range(len(b)):
    b[i]=int(b[i])

#while문 제어
while(True):
    if ~: break
    elif ~: continue

# * 사용 함수
def mul(*values):
    multiply=1
    for i in values:
        multiply=multiply*i
    return multiply
print(mul(5,7,9,10))

list_f=list(str(f)) #숫자f를 str로 만들어 한글자씩 list에
while list_f[-1]=='0' :#맨뒤글자
    del list_f[-1]
value=list_f[-5:]
print(''.join(value)) #value에 있는 값은 리스트이므로 공백기준으로 다시 문자열로

def flatten(data):
    result=[]
    for element in data:
        if type(element)==list: result=result+flatten(element) #type함수
        else: result=result+[element] #리스트 간의 합은 하나의 리스트[리스트1원소들, 리스트2원소들]

#파일 읽고 문장전부 불러오기
f=open("Ch6_Hey_Jude.txt", 'r')
HJ_lyric=f.readlines()
f.close()
contents=""
for line in HJ_lyric:
    contents+=line.strip()+"\n" #한줄씩 문장으로 저장
list=[]
for line in HJ_lytic:
    list.append(line.strip()) #한줄씩 리스트에 저장

#전체단어수 세기(다른 구분자 바꿔주기)
low=contents.lower()
rep=low.replace("-", " ").replace("(", " ").replace(")", " ").replace(",", " ").replace("\n"," ")
sep=rep.split(' ') #바꾼 문자열을 공백을 기준으로 나눔
count=0 #전체 단어수를 저장할 변수
for i in sep:
    if i.islower(): #소문자인 문자열만 count를 증가하도록 함
        count+=1

#단어수 세기 defaultdict 딕셔너리
from collections import defaultdict
count=defaultdict(lambda:0) #횟수를 계산할 변수를 count로 만든후 각 초깃값을 0으로 지정하게함
word=rep2.strip().split() #변환시킨 텍스트인 rep을 한 단어씩 나누어 word에 저장
for i in word: #한 단어씩
    if ' ' in i: continue #만약에라도 단어 중에 ' '공백이 포함된 것이 있다면 단어가 아니므로 count하지 않음
    else: count[i]+=1 #각 단어를 키로 해서 나온횟수 값으로 하는 딕셔너리형

#단어수 정렬 - 딕셔너리형태 (값-횟수기준)
print("상위10개 요소 (단어:횟수): \n", sorted(count.items(), key=lambda t: t[1], reverse=True)[:10], "\n")
print("상위10개 요소 (단어):")
from collections import OrderedDict
for i in OrderedDict(sorted(count.items(), key=lambda t:t[1], reverse=True)[:10]).keys():
    print(i)  #한단어씩 enter로 단어, 횟수 출력

sort_dict={} / output=[]
for k, v in OrderedDict(sorted(total_dict.items(), key=lambda t:t[0], reverse=False)).items(): #ordereddict를 통해 2번에서의 total_dict을 t_name순으로 정렬
    sort_dict.setdefault(k, v)
    #or
    a="{0:<11s} {1:<4s} {2:s}".format(v[0], k, v[1]) #문자열 포매팅을 통해 학번, 이름, 학과 순으로 정리해 a에 저장
    output.append(a)

if sorted(map(int, korean), reverse=True).index(grade)/len(korean) <= 0.3:
    return 'A'
#koreans=list(map(int, koreans))
#korean_sort=sorted(koreans, reverse=True)

#reverse=True(큰 숫자부터), reverse=False(한글 ㄱㄴㄷㄹ..)

from collections import Counter
text=list('gallazed')
c=Counter(text) -> Counter({'a':3, 'b':2...})
b=Counter(a=4, b=2, c=-2) or Counter({'a':4, 'b':2})

print("{:^11s}".format('*' * i)) #가운데정렬
print("{:<11s}".format('*' * i)) #좌측정렬
print("{:>11s}".format('*' * i)) #우측정렬

#mapping & 가격 &역순
#첫번째 방법
price=map(int, input("가격을 ; 로 구분해 입력하세요: ").split(';')) #map함수 사용해 int형으로 나누어 리스트에 저장
sort_p=sorted(price) #입력한 가격을 오름차순으로 정렬
for i in sort_p[::-1]: #오름차순을 역순으로 읽어 내림차순으로 반복
    print('%9s' %format(i, ',')) #금액을 위한 format(숫자, ',')

price=input("가격을 ; 로 구분해 입력하세요: ").split(';') #문자형으로 나누어 리스트에 저장
list=[]
for i in price:
    list.append(int(i)) #int형으로 바꿔 리스트에 넣기
list.sort(reverse=True) #int형 list 값들을 내림차순 정렬. reverse는 역순
for i in list:
    print("{:9,}".format(i)) #금액을 위한 '{:,}'.format(숫자)

큐 : Ch7_3.py

#사방+대각선 검사
for i in range(row):
    for j in range(col):
        for k in range(i - 1, i + 2): #인접한 것이기에 위 아래줄,
            for l in range(j - 1, j + 2): #양옆에 해당하는 요소들을 확인해야함
                if  k < 0 or l < 0 or k >= row or l >= col: #범위 넘은경우

#프린트할 때 옆으로 계속 출력
print(count, end='')

#딕셔너리
dict={}
dict.update(zip(a,b)) #빈 딕셔너리 dict에 a,b 리스트를 a[0]b[0], a[1]b[1].. 을 쌍으로 딕셔너리로 저장해 합침
for key, value in dict.items(): #dict의 key,value를 for문을 돌며 조건 검색
    if key=='delta':
        dict={key: value for key, value in dict.items() if key != 'delta'} #key가 delta인 것 제외하고 dict생성
    elif value==30:
        dict={key: value for key, value in dict.items() if value != 30}  #value가 30인 것 제외하고 dict생성

x={key:valuefor key, value in dict.fromkeys(keys.items())}  #keys는 key로 사용할 리스트
x=dict.fromkeys(키리스트, 기본값)

#리스트원소 나눠서 리스트만들기
int(name[i].split('.')[0])

#학번순 sorting 결과 출력 -format  No.  학번  이름  학과  / 1  xxxxxx1111  홍길동  법학과
print("{0:<3s} {1:<9s} {2:<5s} {3:s}".format("No", "학번", "이름", "학과"))

#reduce & lambda
from functools import reduce
fac=reduce(lambda x, y: x*y, [1,2,3,4,5])
print(reduce(lambda x, y : x+y, list))

f=lambda x: x**2
print(list(map(f, x_list))) = [x**2 for x in x_list]
list(map(lambda x:x**2 if x%2==0 else x, x_list))

# *은 여러개를 동시에 가지고있지만, 하나씩 있다고 생각해주겠다느 의미.  Ch9 행렬 계산pytho

import random
number=random.randint(1,100)

print("%s, %d, %f" %('안녕', 1, 1.0))
print("{0:10d}, {1:s}, {2:10.5f}".format(100, '안녕', 5.24300))

{i+1:j for i,j in enumerate('a bc def g hij'.split())}
