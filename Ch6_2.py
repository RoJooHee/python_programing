#영어 대소문자.띄어쓰기만으로 이루어진 문자열에 단어는 몇개?
#한단어 여러번 등장할 수도 있음

sentence=input("문자열을 입력하세요 : ")
sen=sentence.strip() #문자열의 앞뒤 공백 삭제
voca=sen.split(' ') #문자열 중간의 한칸 띄어쓰기 단어 구분됨
print(len(voca)) #구분된 단어의 개수 출력
