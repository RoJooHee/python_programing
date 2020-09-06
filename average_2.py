kor=[49, 80, 20, 100, 80]
math=[43, 60, 85, 30, 90]
eng=[49, 82, 48, 50, 100]
total_score=[kor, eng, math]

student_sum=[0,0,0,0,0]
student_avrg0=[0,0,0,0,0]
student_avrg1=[0,0,0,0,0]
student_avrg2=[0,0,0,0,0]

for subject in total_score:
    i=0
    for score in subject:
        student_sum[i]+=score
else:
    for j in range(0,i,1):
        student_arg0[j]=student_sum[j]/3

j=0
while(j<1):
    student_avrg1[j]=student_sum[j]/3
    j+=1
