kor=[49, 80, 20, 100, 80]
math=[43, 60, 85, 30, 90]
eng=[49, 82, 48, 50, 100]
studentscore=[0,0,0,0,0]


for i in range(0,5,1):
    studentscore[i]=int((kor[i]+math[i]+eng[i])/3)

print(studentscore)
