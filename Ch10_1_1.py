import pandas as pd

df = pd.read_csv('파이썬프로그래밍01반_CSV.csv', engine='python')

name = df['이름'].values
number = df['학번(ID)'].values
department = df['소속명'].values
math = df['Math'].values
english = df['English'].values
korean = df['Korean'].values

class Student:
    def __init__(self, name, number, department, math, english, korean):
        self.name = name
        self.number = number
        self.department = department
        self.math = math
        self.english = english
        self.korean = korean


    def show_info(self):
        print(("{:<9}{:^15}{:^25}".format(self.name, self.number, self.department)), end='\t')

    def calc_sum(self):
        sum = int(self.math) + int(self.english) + int(self.korean)
        return sum

    def calc_aver(self):
        avg = (int(self.math) + int(self.english) + int(self.korean)) / 3
        return round(avg, 1)

    def calc_grade(self, sub):
        if sub=="korean":
            grade = int(self.korean)
            if sorted(map(int, korean), reverse=True).index(grade)/len(korean) <= 0.3:
                return 'A'
            elif sorted(map(int, korean), reverse=True).index(grade)/len(korean) <= 0.7:
                return 'B'
            else:
                return 'C'

        elif sub=="math":
            grade = int(self.math)
            if sorted(map(int, math), reverse=True).index(grade)/len(math) <= 0.3:
                return 'A'
            elif sorted(map(int, math), reverse=True).index(grade)/len(math) <= 0.7:
                return 'B'
            else:
                return 'C'

        elif sub=="english":
            grade = int(self.english)
            if sorted(map(int, english),reverse=True).index(grade)/len(english) <= 0.3:
                return 'A'
            elif sorted(map(int,english), reverse=True).index(grade)/len(english) <= 0.7:
                return 'B'
            else:
                return 'C'

objs = [ Student(b, c, d, e, f, g) for b, c, d, e, f, g in zip(name, number, department, math, english, korean) ]

students = sorted(objs, key = lambda x: -x.calc_sum())
print(" ############################################### 2번 ############################################### ")
print("{:<9}{:^6}  {:^15}{:^25}\t\t{:^9}{:^9}".format("No", "이름", "학번", "학과", "총점", "평균"))
for i, j in enumerate(students):
    print('{:<9}'.format(i+1), end='')
    j.show_info()
    print('{:^9}'.format(j.calc_sum()),end='')
    print('    {:^9}'.format(j.calc_aver()), end='')
    print()
print(" ################################################################################################### \n\n\n")


print(" ############################################### 3번 ############################################### ")
scores = sorted(objs, key = lambda x: x.name)
print("{:>9}{:>9}{:>20}    {:>9}{:>9}{:>9}".format("No", "이름", "학번", "수학", "영어", "국어"))
for i,j in enumerate(scores):
    print('{:>9}'.format(i+1), end='')
    print('{:>9}'.format(j.name), end='')
    print('     {:>20}'.format(j.number), end='')
    print('{:>9}'.format(j.calc_grade("math")), end='')
    print('   {:>9}'.format(j.calc_grade("english")), end='')
    print(' {:>9}'.format(j.calc_grade("korean")), end='')
    print()
print(" ################################################################################################### \n\n\n")
