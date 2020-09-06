#대한민국헌법_1장.txt 읽어들인 후
#counter 모듈 이용해 본문에 사용된 단어의 사용빈도수 구함
#가장 빈번히 사용된 단어 10개 출력.   collections 모듈함수 사용

f=open("대한민국헌법_1장.txt", 'r')
text=f.readlines()
f.close()

contents=""
for line in text:
    contents+=line.strip()+"\n"

rep1=contents.replace("[", " ").replace("]", " ").replace("<", " ").replace(">", " ").replace(",", " ").replace("\n"," ").replace(".", " ").replace("ㆍ", " ")
rep2=rep1.replace("①", " ").replace("②", " ").replace("③", " ").replace("④", " ").replace("⑤", " ").replace("⑥", " ").replace("⑦", " ")

from collections import defaultdict
count=defaultdict(lambda:0) #횟수를 계산할 변수를 count로 만든후 각 초깃값을 0으로 지정하게함

word=rep2.strip().split() #변환시킨 텍스트인 rep을 한 단어씩 나누어 word에 저장
for i in word: #한 단어씩
    if ' ' in i: continue #만약에라도 단어 중에 ' '공백이 포함된 것이 있다면 단어가 아니므로 count하지 않음
    else: count[i]+=1 #각 단어 나온횟수 딕셔너리형

print("본문에 사용된 단어의 사용빈도수 : \n", count, "\n")

print("상위10개 요소 (단어:횟수): \n", sorted(count.items(), key=lambda t: t[1], reverse=True)[:10], "\n")
#이렇게 써도 가능 from collections import Counter        \n        print(Counter(word).most_common(10))

print("상위10개 요소 (단어):")
from collections import OrderedDict
for i in OrderedDict(sorted(count.items(), key=lambda t:t[1], reverse=True)[:10]).keys():
    print(i)  #한단어씩 enter로 단어, 횟수 출력
