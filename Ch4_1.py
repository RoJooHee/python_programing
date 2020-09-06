year=int(input("몇년도에 태어나셨나요?: "))
#띠를 먼저 리스트로 선언함
ddi=['쥐', '소', '범', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개' , '돼지']

#띠 순서를 year을 12로 나눈 나머지에 따라 정함
order=year%12

if order==0: print(ddi[8])
elif order==1: print(ddi[9])
elif order==2: print(ddi[10])
elif order==3: print(ddi[11])
elif order==4: print(ddi[0])
elif order==5: print(ddi[1])
elif order==6: print(ddi[2])
elif order==7: print(ddi[3])
elif order==8: print(ddi[4])
elif order==9: print(ddi[5])
elif order==10: print(ddi[6])
else: print(ddi[7])

print("띠 입니다.")
