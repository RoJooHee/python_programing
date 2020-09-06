#이름, 학번(ID), 소속명, Math, English, Korean
f=open("파이썬프로그래밍01반_CSV.csv", 'r')
text=f.readlines()
f.close()

contents=[]
all=[]
for line in text:
    contents=line.strip().split(",") #각 학생별로 , 기준으로 나눠 데이터 저장
    all.append(contents) #all을 모든 학생들 정보 넣은 다차원리스트로 만듦
del all[0] #제목에 해당하는 부분 삭제

class Student:
    def __init__(self, name, number, department, math, english, korean):
        self.name=name
        self.number=number
        self.department=department
        self.math=math
        self.english=english
        self.korean=korean

    def show_info(self, name, number, department):
        return self.name, self.number, self.department

    def calc_sum(self, math, english, korean):
        sum=int(self.math)+int(self.english)+int(self.korean)
        return sum

    def calc_aver(self, math, english, korean):
        aver=(int(self.math)+int(self.english)+int(self.korean))/3
        average=round(aver,1)
        return average

    def calc_grade(self, math): #41명 상위30% =12.3/ 상위30~70% =28.7/ 상위70~100%. 동점인 경우 상위grade로
        global maths
        maths=list(map(int, maths))
        math_sort=sorted(maths, reverse=True)
        if int(self.math)>=math_sort[11]: return "A" #~12명(0~11)
        elif int(self.math)>=math_sort[27]: return "B" #~28명(~27)
        else : return "C" #~나머지

    def calc_grade(self, english): #41명 상위30% =12.3/ 상위30~70% =28.7/ 상위70~100%. 동점인 경우 상위grade로
        global englishs
        englishs=list(map(int, englishs))
        english_sort=sorted(englishs, reverse=True)
        if int(self.english)>=english_sort[11]: return "A" #~12명(0~11)
        elif int(self.english)>=english_sort[27]: return "B" #~28명(~27)
        else : return "C" #~나머지

    def calc_grade(self, korean): #41명 상위30% =12.3/ 상위30~70% =28.7/ 상위70~100%. 동점인 경우 상위grade로
        global koreans
        koreans=list(map(int, koreans))
        korean_sort=sorted(koreans, reverse=True)
        if int(self.korean)>=korean_sort[11]: return "A" #~12명(0~11)
        elif int(self.korean)>=korean_sort[27]: return "B" #~28명(~27)
        else : return "C" #~나머지

    def __str__(self):
        return " %s Student 객체 생성됨" %(self.name)

#1번문항
print("1번문항 - 인스턴스 생성\n")
#학생의 속성 각각을 리스트로 만듦
student_list=[]
names=[] ; numbers=[] ; departments=[] ;maths=[] ; englishs=[] ; koreans=[]
for stu in all:
    names.append(stu[0])
    numbers.append(stu[1])
    departments.append(stu[2])
    maths.append(stu[3])
    englishs.append(stu[4])
    koreans.append(stu[5])

#학생 전체 객체 생성 student_list에 객체 하나씩 넣어놓음
for name, number, department, math, english, korean in zip(names, numbers, departments, maths, englishs, koreans):
    stu=Student(name, number, department, math, english, korean)
    print(stu)
    student_list.append(stu)

#2번문항
print("\n \n 2번문항 - 총점 내림차순으로 총점&평균 \n")
#학생 총점 sums
sums=[]
for i in range(len(student_list)):
    a=student_list[i].calc_sum(math, english, korean)
    sums.append(a)

#학생 평균 점수 avers
avers=[]
for i in range(len(student_list)):
    a=student_list[i].calc_aver(math, english, korean)
    avers.append(a)

#학생 이름, 학번, 학과 students(클래스 메서드)
students=[]
for i in range(len(student_list)):
    a=student_list[i].show_info(name, number, department)
    students.append(a)

#2번에 필요한 전체 정보들을 학생별로 리스트 만듦. sums 점수 기준으로 내림차순.
all=[]
for a in zip(students, sums, avers):
    all.append(a)
all_sort=sorted(all, key=lambda x:x[2], reverse=True)

print("{0:<2s} {1:<5s} {2:<11s} {3:<18s} {4:<4s} {5:<4s}".format("No", "이름", "학번", "학과", "총점", "평균"))

#students에 name, number, department 포함되어있으므로 이차원리스트로 접근.
q2=[]
for i in range(len(student_list)):
    for one in all_sort:
        a="{0:<4s} {1:<13s} {2:<15s} {3:<6d} {4:<4.1f}".format(one[0][0], one[0][1], one[0][2], one[1], one[2])
        q2.append(a)
    #No번호
    b="{0:<2d} {1:s}".format(i+1, q2[i])
    print(b)

#3번문항
print("\n \n 3번문항 - 이름 오름차순으로 각 과목 학점 \n")
#수학 학점 m(클래스 메서드)
m=[]
for i in range(len(student_list)):
    a=student_list[i].calc_grade(math)
    m.append(a)

#영어 학점 e(클래스 메서드)
e=[]
for i in range(len(student_list)):
    a=student_list[i].calc_grade(english)
    e.append(a)

#국어 학점 k(클래스 메서드)
k=[]
for i in range(len(student_list)):
    a=student_list[i].calc_grade(korean)
    k.append(a)

#3번에 필요한 전체 정보들을 학생별로 리스트 만듦. names 기준으로 오름차순.
all=[]
for a in zip(names, numbers, m, e, k):
    all.append(a)
all_sort=sorted(all, key=lambda x:x[0], reverse=False)

print("{0:<2s} {1:<5s} {2:<11s} {3:<3s} {4:<3s} {5:<3s}".format("No", "이름", "학번", "수학", "영어", "국어"))

q3=[]
for i in range(len(student_list)):
    for one in all_sort:
        a="{0:<4s} {1:<13s} {2:<5s} {3:<5s} {4:<5s}".format(one[0], one[1], one[2], one[3], one[4])
        q3.append(a)
    #No번호
    b="{0:<2d} {1:s}".format(i+1, q3[i])
    print(b)
