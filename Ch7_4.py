#표준입력으로 2차원리스트 가로col 세로row입력, 그다음줄 부터 리스트의 요소로 들어갈 문자 입력
#2차원리스트 안에서 *지뢰. .은x. 지뢰가 아닌 요소에는 인접한 지뢰의 개수 출력하는 프로그램
#matrix=[]  for I in range(row): matrix.append(list(input())) 사용

col, row = input("가로 세로 개수 입력하세요 : ").split()
col=int(col)
row=int(row)

matrix=[]
for I in range(row):
    matrix.append(list(input()))  #문자 입력하고 enter누르면 한 col 완성. row 개수만큼 반복하면서 2차원리스트 완성

for i in range(row):
    for j in range(col): #위에서 리스트 만들때 col길이가 길어져도 여기에서 제한함
        if matrix[i][j] == "*" :
            print('*', end='')  #i줄에 j번째 인덱스가 *이면 지뢰이므로 그대로 출력

        elif matrix[i][j] =="." :  #i줄에 j번째 인덱스가 .이면 인접한 지뢰개수 출력
            count = 0  #지뢰개수를 count에 저장할 것
            #인접한 요소들의 지뢰개수 확인하는 중첩for문
            for k in range(i - 1, i + 2): #인접한 것이기에 위 아래줄,
                for l in range(j - 1, j + 2): #인양옆에 해당하는 요소들을 확인해야함
                    if  k < 0 or l < 0 or k >= row or l >= col:
                        continue  #반복문범위가 개수범위 초과하는 경우 예외처리로 넘김
                    elif matrix[k][l]=='.':
                        count=count+0  #근접한 요소가 .이면 count에는 변함없음
                    elif matrix[k][l] == "*":
                        count=count+1  #근접한 요소 중 *이 있으면 지뢰개수 count 1 증가
                    else : continue #그 외의 입력이 있는 경우 오류이므로 건너뜀
            print(count, end='')

        else : continue #그 외의 입력 있는 경우 오류이므로 건너뜀

    print()
