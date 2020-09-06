#Hey Jude가사파일에서 1.Jude 단어횟수 2.Na/na 단어횟수 3.단어변경 Jude->내이름 전체출력

f=open("Ch6_Hey_Jude.txt", 'r')
HJ_lyric=f.readlines()
f.close()

contents=""
for line in HJ_lyric:
    contents+=line.strip()+"\n"
num_j=contents.count("Jude") #1번
num_n=contents.lower().count("na") #2번
#num_N=contents.count("Na")+contents.count("na")
change=contents.replace("Jude", "JooHee") #3번

print("Jude 횟수:", num_j, " / Na&na 횟수:", num_n)
print("이름 변경 \n", change)
