#표준 입력으로 물품가격 여러개가 문자열 한줄로 입력되고 ; 로 구분됨
#높은 가격순으로 출력. 가격 길이는 9고 천단위마다 ,넣기 (_,___,___)

#첫번째 방법
price=map(int, input("가격을 ; 로 구분해 입력하세요: ").split(';')) #map함수 사용해 int형으로 나누어 리스트에 저장
sort_p=sorted(price) #입력한 가격을 오름차순으로 정렬

for i in sort_p[::-1]: #오름차순을 역순으로 읽어 내림차순으로 반복
    print('%11s' %format(i, ',')) #금액을 위한 format(숫자, ',')


#2번째 방법
price=input("가격을 ; 로 구분해 입력하세요: ").split(';') #문자형으로 나누어 리스트에 저장

list=[]
for i in price:
    list.append(int(i)) #빈 리스트에 price값을 int형으로 추가
list.sort(reverse=True) #int형 list 값들을 내림차순 정렬. reverse는 역순

for i in list:
    print("{:11,}".format(i)) #금액을 위한 '{:,}'.format(숫자)
