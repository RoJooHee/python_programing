#파이썬1_수강생_이름.txt 파이썬1_수강생_학번.txt 파이썬1_수강생_학과.txt 3개파일로

name=open("파이썬1_수강생_이름.txt", 'r')
num=open("파이썬1_수강생_학번.txt", 'r')
major=open("파이썬1_수강생_학과.txt", 'r')
text_name=name.readlines() #파일을 읽어옴
text_num=num.readlines()
text_major=major.readlines()
name.close()
num.close()
major.close()

t_name=[]
for line in text_name:
    t_name.append(line.strip()) #파일을 읽어와 한줄씩 리스트에 저장
t_num=[]
for line in text_num:
    t_num.append(line.strip())
t_major=[]
for line in text_major:
    t_major.append(line.strip())

#1번 파일 하나씩 읽어 3개의 별도 리스트 만들고, 통합리스트 만들어출력  total_list = [(‘홍길동’, xxxxxx1111, ‘법학과’)..]
total_list=[]
for i in range(len(t_name)):
    t=(t_name[i], t_num[i], t_major[i]) #각 파일의 같은 인덱스끼리 읽어와 한 튜플로 만들어서, 리스트 차례로 저장
    total_list.append(t)
print("total_liast = ", total_list, "\n")

#2번 key:이름, value:학번,학과  딕셔너리 만들고 출력 total_dict = {‘홍길동’:[xxxxxx1111,‘법학과’], ...}
num_major=[]
total_dict={}
for i in range(len(t_name)):
    t=[t_num[i], t_major[i]] #각 사람의 학번과 학과를 한 리스트에 저장해서 num_major 리스트에 차례로 저장
    num_major.append(t)
    total_dict.setdefault(t_name[i], num_major[i]) #딕셔너리에 키는 이름, 값은 [학번, 학과]으로  키-값 쌍 추가
print("total_dict = ", total_dict, "\n")

#3번 이름순 sorting 딕셔너리 만들고 출력  sort_dict = {‘이순신’:[xxxxxx2222,‘경영학과’],...}
from collections import OrderedDict
sort_dict={}
for k, v in OrderedDict(sorted(total_dict.items(), key=lambda t:t[0], reverse=False)).items(): #ordereddict를 통해 2번에서의 total_dict을 t_name순으로 정렬
    sort_dict.setdefault(k, v) #정렬 후 키와 값을 차례로 새로운 딕셔너리에 키-값 쌍 추가
print("sort_dict = ", sort_dict, "\n")

#4번 학번순 sorting 결과 출력 -format  No.  학번  이름  학과  / 1  xxxxxx1111  홍길동  법학과
print("{0:<3s} {1:<9s} {2:<5s} {3:s}".format("No", "학번", "이름", "학과"))

output=[]
for i in range(len(sort_dict)):
    for k, v in OrderedDict(sorted(total_dict.items(), key=lambda t:t[1], reverse=False)).items(): #3번과는 달리 학번순 정렬해 t[1]로 바꿈. (학번 학과 순으로 저장해서 학번 순 정렬됨)
        a="{0:<11s} {1:<4s} {2:s}".format(v[0], k, v[1]) #문자열 포매팅을 통해 학번, 이름, 학과 순으로 정리해 a에 저장
        output.append(a) #딕셔너리 키-값 쌍 개수만큼 반복되며 output 리스트에 저장됨
    print("{0:<3d} {1:s}".format(i+1, output[i])) #No. 번호 지정위해 키-값 쌍 개수만큼 돌면서 i+1로 1부터 번호 지정하게 하며, 문자열포매팅 통해 No.번호와 output 정리해 출력
