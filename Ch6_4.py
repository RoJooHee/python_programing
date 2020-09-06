#format메서드 이용해서 *를 1,3,5,7,9,11 가운데정렬 삼각형 출력

for i in range(1, 12, 2):
    print("{:^11s}".format('*' * i)) #맨밑줄이 11자리이므로 11개 여유공간 지정. *은 i개씩 출력
for i in range(1, 12, 2):
    print("{:>11s}".format('*' * i))
for i in range(1, 12, 2):
    print("{:<11s}".format('*' * i))
