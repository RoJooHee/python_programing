import time
class Student(object):
    def __init__(self, name, ID, password, profile):
        self.name = name
        self.ID = ID
        self.__password = password
        self.profile = profile

    def create_member(self, name): #회원가입
        a = " - " + self.name + "님 (ID: " + self.ID + ", 학교/학년: " + self.profile + ") 회원가입 완료되었습니다. -"
        print(a)

    def update_member_info(self, password, profile): #회원정보 업데이트
        self.__password = password
        self.profile = profile
        print("\n "+self.name + " 님의 비밀번호 변경완료. 변경된 학년은 " + self.profile)

    def remove_member(self, name): #회원객체 하나 삭제
        print(" -'" + self.name + "' 학생의 계정이 탈퇴됩니다.-")

    def show_member_info(self, name): #회원정보 보여줌
        a = " 이름: {0:<s}  /  ID: {1:<s}  /  학교/학년: {2:<s}".format(self.name, self.ID, self.profile)
        print(a)

    def check_password(self, password): #패스워드가 일치하는지 확인
        if self.__password == password:
            return 1
        else:
            return 0

    def login(self, ID, password): #로그인
        if self.ID == ID and self.__password == password:
            print(" << " + self.name + "학생 로그인 되었습니다. >>")
            return 1
        else:
            return 0

class Timeline(object):
    def __init__(self, writer, time, title, note, tag, goodfriend, message):
        self.writer = writer
        self.time = time
        self.title = title
        self.note = note
        self.tag = tag
        self.goodfriend = goodfriend
        self.message = message

    def input_timeline(self, writer, time): #타임라인 글올리기
        a = "\n  질문자: {0}  /  게시일자: {1}-{2}-{3}\n  제목: {4}".format(self.writer, self.time.tm_year, self.time.tm_mon, self.time.tm_mday, self.title)
        print(a + "\n\n 글이 업로드 되었습니다.")

    def remove_timeline(self, writer, title): #글쓴이+제목 맞을 때삭제
        if (self.writer == writer) and (self.title == title):
            print(" -'" + self.title + "' 글이 삭제됩니다.-")
            return 1
        else:
            return 0

    def remove_timelines(self, writer): #글쓴이가 쓴 글 삭제
        if self.writer == writer:
            return 1

    def show_timeline(self, title): #타임아린 보여주기
        print("\n  | 질문자: {0}  /  게시일자: {1}-{2}-{3}  /  ♡: {4}".format(self.writer, self.time.tm_year, self.time.tm_mon, self.time.tm_mday, self.goodfriend))
        print("  | 제목: {0}\n  | 내용: {1}".format(self.title, self.note))
        print("  | 태그 :", end = ' ')
        for i in range(len(self.tag)):
            print(self.tag[i], end = ' ')
        print("\n")
        for i in range(len(self.message)): #댓글
            print("     -> " + self.message[i])
        print("\n ---------------------------------------------------------------------")
