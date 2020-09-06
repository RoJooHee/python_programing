from Simple_SNS import Student
from Simple_SNS import Timeline
import time
import csv

swear_list=[]
with open("swearword_list.csv", "r", encoding = "cp949") as swear: #csv파일로 욕설에 대해 리스트로 저장
    while 1:
        swear_temp = swear.readline()
        if not swear_temp:
            break
        else :
            swear_list_temp = swear_temp.split(",")
            for i in range(len(swear_list_temp)):
                swear_list.append(swear_list_temp[i])

student_list = []
line_list = []
print(" <<< 학생용 질문 서비스에 오신 것을 환영합니다 >>>")
go = input(" 실행하시겠습니까? (네) - ")
login_yn = 0
login_index = -1

while(go == '네') : #실행 중
    if login_yn == 0: #로그인 안된 상태
        answer = input("\n 로그인 또는 회원가입 중에 무엇을 원하시나요? : ")
        if answer == '로그인':
            id = input("\n 이메일   입력 : ")
            password = input(" 비밀번호 입력 : ")
            for i in range(len(student_list)): #for문 돌면서 id,password가 맞는 객체 찾기
                login_yn = student_list[i].login(id, password) #맞는 객체 찾으면 로그인되어서 login_yn=1 반환
                if login_yn == 1:
                    login_index = i #로그인 된 객체의 i 인덱스 알아냄
                    break

            if login_yn == 0:
                print(" 로그인 실패")

        elif answer == '회원가입' :
            name = input("\n 이름      입력 : ")
            id = input(" 아이디    입력 : ")
            for i in range(len(student_list)): #아이디가 기존 회원과 중복될 시 재입력
                while (student_list[i].ID == id):
                    id = input(" 아이디  재입력 : ")
            password = input(" 비밀번호  입력 : ")
            profile = input(" 학교/학년 입력 : ")
            stu = Student(name, id, password, profile) #객체는 stu
            student_list.append(stu) #객체들의 리스트 student_list
            stu.create_member(name) #회원가입된 회원 정보 확인
            #다시 로그인/회원가입 창으로

        else:
            print(" -다시 입력해주세요.-")

    elif login_yn == 1: #로그인 된 상태
        print("\n")
        if len(line_list) == 0:
            print(" -타임라인이 비어있습니다.-\n")
        else:
            print("\n\n <<현재 타임라인>>")
            for i in range(len(line_list)-1, -1, -1):
                line_list[i].show_timeline(line_list[i].title) #현재 타임라인 출력

        question = input("\n 1.타임라인으로  /  2. 본인의 회원정보로  /  3. 모든 회원의 정보  /  4. 그만! : ")
        if question == '1': #타임라인으로
            choice = input(" 1. 질문 작성  /  2. 자신의 질문 삭제  /  3.  타임라인 질문 찾기 or 코멘트 : ")

            if choice == '1': #타임라인 글 작성
                writer = student_list[login_index].name #글쓴이는 아까 로그인 한 회원의 이름
                title = input("\n 질문 제목: ")
                note = input(" 질문 내용: ")
                tag = input(" 태그(공백으로 구분): ").split( ) #공백 기준으로 tag 리스트 형태로
                for i in range(len(tag)):
                    tag[i] = "#" + tag[i]
                goodfriend = 0
                message = []
                line = Timeline(writer, time.localtime(), title, note, tag, goodfriend, message) #타임라인글 객체 line 생성
                line_list.append(line) #객체들을 line_list 배열에 저장
                line.input_timeline(writer, time) #타임라인을 보여주는 함수

            elif choice == '2': #자신의 글 삭제
                delete = 0
                writer1 = student_list[login_index].name
                title1 = input("\n 삭제하고 싶은 자신의 질문 제목 : ")
                for i in range(len(line_list)):
                    if (line_list[i].remove_timeline(writer1, title1) == 1): #글쓴이와 글제목으로 삭제함수 호출
                        delete = 1
                        del line_list[i] #함수의 조건에 부합하여 1이 반환되면 해당 글 삭제
                        break
                if delete == 0: #만약 삭제할 글이 없어 0이 계속 반환된 경우
                    print("\n- 삭제할 질문이 존재하지 않습니다.-")

            elif choice == '3': #타임라인 질문 찾기 or 코멘트
                choice = input("\n 1. 원하는 질문 찾기  /  2. 좋아요 or 댓글 달기 : ")

                if choice == '1': #원하는 질문 찾기
                    want=input("\n 원하는 질문의 태그를 입력하세요 : ")
                    for i in range(len(line_list)): #각 글마다(i) 태그들을(j) 돌면서 해당 태그가 있는 글만 보여줌
                        for j in range(len(line_list[i].tag)):
                            if want in line_list[i].tag[j]:
                                line_list[i].show_timeline(line_list[i].title)
                    print(" ---------------------------------------------------------------------\n")

                elif choice == '2':
                    choose = 0
                    comment_writer = input("\n 질문의 글쓴이를 입력하세요 : ")
                    comment_title = input(" 질문의 제목을 입력하세요 : ")
                    for i in range(len(line_list)):
                        if line_list[i].title == comment_title and line_list[i].writer == comment_writer: #만약 위에서 입력한 제목의 글이 있다면
                            choose = 1
                            comment = input(" 1. 좋아요  /  2. 댓글 : ")
                            if comment == '1': #좋아요의 경우는 +1
                                line_list[i].goodfriend += 1
                            elif comment == '2': #댓글은 리스트에다가 댓글을 추가함
                                msg = input(" 남기고 싶은 댓글을 입력하세요 : ")
                                msg_temp = 0
                                for s in range(len(swear_list)): #맨 위에서 리스트로 만들었던 욕설 단어들
                                    if swear_list[s] in msg: #만약 달려는 댓글에 욕이 포함되어 있으면 댓글 작성 안됨
                                        print("\n -욕설이 포함된 댓글은 작성할 수 없습니다.-")
                                        msg_temp = 1
                                        break
                                if msg_temp == 0:
                                    line_list[i].message.append(msg)

                    if choose == 0: #위에서 입력한 제목의 글이 존재하지 않는다면
                        print("\n -해당 질문은 존재하지 않습니다.-")

        elif question == '2':  #본인의 회원정보로
            check = input("\n 본인확인을 위해 기존 비밀번호를 입력해주세요 : ") #본인확인으로 비밀번호가 맞아야 본인 회원정보에 접근 가능
            if student_list[login_index].check_password(check) == 1:
                choice = input(" 1. 회원정보 수정  /  2. 회원 탈퇴 : ")

                if choice == '1': #회원정보 수정
                    password = input(" 비밀번호  수정: ")
                    profile = input(" 학교/학년 수정: ")
                    student_list[login_index].update_member_info(password, profile) #입력한 값으로 비밀번호, 학년 수정

                if choice == '2': #회원 탈퇴
                    delete = 0
                    writer1 = student_list[login_index].name
                    delete_index = []
                    for i in range(len(line_list)): #먼저 지금 로그인한 학생이 작성한 타임라인의 글들을 모두 제거함
                        if (line_list[i].remove_timelines(writer1) == 1): #만약 글쓴이와 현재 로그인 한 사람이 같은 경우에 그 글의 inddex 저장
                            index = i
                            delete_index.append(index)
                            delete = 1

                    for a in range(0, len(delete_index), 1): #삭제할 글의 인덱스를 돌며 line_list에서 삭제
                        del line_list[delete_index[a]] #글 하나를 삭제하면 line_list에서 뒷부분의 인덱스가 하나씩 앞으로 당겨짐
                        if (a != len(delete_index) - 1): #그래서 맨 마지막 삭제가 아니라면, 글 삭제 후 delete_index를 하나씩 작게해야함
                            for b in range(a, len(delete_index), 1):
                                delete_index[b] = delete_index[b] - 1

                    if delete == 1: #하나라도 제거할 글이 있었다면 이 문구 출력
                        print(" -'" + writer1 + "' 학생의 질문이 전부 삭제되었습니다.-")

                    student_list[login_index].remove_member(name) #그 후 로그인한 학생을 회원 리스트에서 삭제하며 탈퇴
                    del student_list[login_index]
                    login_yn = 0

            else:
                print("\n -회원정보 수정이 불가합니다.-") #본인확인을 위한 비밀번호가 틀린경우 접근 불가

        elif question == '3':  #가입된 모든 회원의 정보 보여줌
            for i in range(len(student_list)):
                student_list[i].show_member_info(student_list[i].name)

        elif question == '4':  #그만!
            choice = input(" 1. 로그아웃 / 2. 종료 : ")

            if choice == '1': #로그아웃
                print(" -로그아웃 됩니다.-")
                login_yn = 0

            elif choice == '2': #종료
                print(" -종료합니다.-")
                break

        else : print(" -다시 입력해주세요.-")
