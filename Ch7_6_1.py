f = open("대한민국헌법_1장.txt", "r")
lines = f.read()

from konlpy.tag import Twitter
nlpy = Twitter()
nouns = nlpy.nouns(lines)
print(nouns)

from collections import Counter
count = Counter(nouns)
tag_count = []
tags = []
for n, c in count.most_common(100):
    dics = {'tag': n, 'count': c}
    if len(dics['tag']) >= 2 and len(tags) <= 49:
        tag_count.append(dics)
        tags.append(dics['tag'])

for tag in tag_count:
    print(" {:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))

------------------------------------------------------------------

f=open("대한민국헌법_1장.txt", 'r')
text=f.readlines()
f.close()

from collections import defaultdict
count=defaultdict(lambda:0)

for line in text:
    word=line.strip().split()

    for i in word :
        count[i]+=1

#txt를 각 문장씩 반복하고, 각 문장의 한 단어씩 all이라는 리스트에 넣음
#, [, ], 원형숫자 같은거 어떻게 제외시킬지? 그냥 공백만들기?

from collections import OrderedDict
for i, v in OrderedDict(sorted(count.items(), key=lambda t:t[1], reverse=True)).items():
    print(i,v)

result=sorted(count.items(), key=lambda t:t[1], reverse=True)
print(result[:10])
