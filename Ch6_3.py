#Hey_Jude 파일 가사의 전체 단어수 세서 출력. 구분자는 공백 - , ( )
#같은 단어도 나온 횟수만큼 세기

f=open("Ch6_Hey_Jude.txt", 'r')
HJ_lyric=f.readlines()
f.close()

contents=""
for line in HJ_lyric:
    contents+=line.strip()+"\n" #content에 가사 한줄씩 좌우공백 삭제하며 저장

low=contents.lower()
rep=low.replace("-", " ").replace("(", " ").replace(")", " ").replace(",", " ").replace("\n"," ")
#단어를 구분할 모든 구분자들을 공백으로 바꿈
#\n도 문자열이 아닌 구분자 역할이므로 공백으로 바꿈
sep=rep.split(' ') #바꾼 문자열을 공백을 기준으로 나눔

count=0 #전체 단어수를 저장할 변수
for i in sep:
    if i.islower(): #소문자인 문자열만 count를 증가하도록 함
        count+=1
#구분자 여러개가 함께 있을시 공백이 여러개가 되어, 공백도 문자열로서 인식되기 때문

print(count)
