import re
import os
from bs4 import BeautifulSoup
from datetime import datetime

class_ = []
id_ = []
pwd = []
name = []
age = []
nickname = []
birth = []
friend = []

total_posts = 0
posts = []
writer = [] # 게시자만 저장
date = [] # 게시일 저장
authority = [] # 읽기 권한 소유자 아이디 저장
title = [] # 타이틀만 저장
main = [] # 메인만 저장
addition = [] # 좋아요 수, 뎃글 수 저장
comment = [] # 뎃글 저장
text_timeline = []

num_good = []
num_comment = []

# 현재 members 폴더에 존재하는 member 개수 반환하는 함수
def num_member():
    file_list = os.listdir('./members')
    num_member = [file for file in file_list if file.endswith(".txt")]
    return(len(num_member))

tot_mem = num_member()

# 멤버 정보 로딩하는 함수
def loading():
    for i in range(tot_mem):
        with open('./members/member{}.txt'.format(i), 'r', encoding='utf-8') as f:
#             global class_, id_, pwd, name, age, nickname, birth, friend
            txt = f.readlines()

            # class 파싱
            tmp = re.search('<class.*/class>', str(txt), re.I|re.S)
            class_.append(re.sub('</*class>', '', tmp.group(), 0, re.I|re.S))

            # id 파싱
            tmp = re.search('<id.*/id>', str(txt), re.I|re.S)
            id_.append(re.sub('</*id>', '', tmp.group(), 0, re.I|re.S))

            # pwd 파싱
            tmp = re.search('<pwd.*/pwd>', str(txt), re.I|re.S)
            pwd.append(re.sub('</*pwd>', '', tmp.group(), 0, re.I|re.S))

            # 이름 파싱
            tmp = re.search('<name.*/name>', str(txt), re.I|re.S)
            name.append(re.sub('</*name>', '', tmp.group(), 0, re.I|re.S))

            # age 파싱
            tmp = re.search('<age.*/age>', str(txt), re.I|re.S)
            age.append(re.sub('</*age>', '', tmp.group(), 0, re.I|re.S))

            # nickname 파싱
            tmp = re.search('<nickname.*/nickname>', str(txt), re.I|re.S)
            nickname.append(re.sub('</*nickname>', '', tmp.group(), 0, re.I|re.S))

            # birth 파싱
            tmp = re.search('<birth.*/birth>', str(txt), re.I|re.S)
            birth.append(re.sub('</*birth>', '', tmp.group(), 0, re.I|re.S))

            # friend 파싱
            tmp = re.search('<friend.*/friend>', str(txt), re.I|re.S)
            friend.append(re.sub('</*friend>', '', tmp.group(), 0, re.I|re.S))


# 로그인 함수
def login():
    global id_
    for j in range(5):
        ID = input('ID >> ')
        PWD = input('Password >> ')
        for i in range(tot_mem):
            if  ID == id_[i] and PWD == pwd[i]:
                return i
        print('ID 혹은 Password가 일치하지 않습니다.\n')
    return -1

# 회원가입 함수
def assignment():
    global tot_mem
    global id_
    new_id = input('ID : ')
    new_pass = input('Password : ')
    new_name = input('Name : ')
    new_age = input('Age : ')
    new_nickname = input('Nickname : ')
    new_birth = input('Birth day (YYYYMMDD): ')
    if new_id in id_:
        print('이미 존재하는 ID 입니다.')
        return -1
    else :
        print('회원가입이 완료 되었습니다.')
        with open('./members/member{}.txt'.format(tot_mem),'w',
                  encoding='utf-8') as f:
            f.write('<class>' + str(tot_mem) + '</class>\n')
            f.write('<id>' + new_id + '</id>\n')
            f.write('<pwd>' + new_pass + '</pwd>\n')
            f.write('<name>' + new_name + '</name>\n')
            f.write('<age>' + new_age + '</age>\n')
            f.write('<nickname>' + new_nickname + '</nickname>\n')
            f.write('<birth>' + new_birth + '</birth>\n')
            f.write('<friend>' +' '+ '</friend>\n')
            loading()
    tot_mem += 1

# 게시물 로딩하는 함수
def loading_posts():

    global total_posts
    global text_timeline

    global posts
    global writer
    global date
    global authority
    global title
    global main
    global addition
    global comment
    global text_timeline
    global num_good
    global num_comment

    total_posts = 0
    posts = []
    writer = [] # 게시자만 저장
    date = [] # 게시일 저장
    authority = [] # 읽기 권한 소유자 아이디 저장
    title = [] # 타이틀만 저장
    main = [] # 메인만 저장
    addition = [] # 좋아요 수, 뎃글 수 저장
    comment = [] # 뎃글 저장
    text_timeline = []

    num_good = []
    num_comment = []

    with open ('temp.txt'.format(0), 'r', encoding='utf-8') as f:
        tmp = f.readlines()
#         print(tmp)
        tmp2 = re.search(r'@@total_posts@@(\d+)@@total_posts@@', str(tmp))
        total_posts = int(tmp2.groups(1)[0])
#         print('총 게시물 수 :', total_posts) # 총 게시물 수 loading

        soup = BeautifulSoup(str(tmp), 'html.parser')

        # 게시자(writer) 파싱
        writers = soup.findAll('writer')
        for i in writers:
            writer.extend(BeautifulSoup(str(i),'html.parser').find('writer'))
#         print('게시자 :', writer)

        # 게시일(date) 파싱
        dates = soup.findAll('date')
        for i in dates:
            date.extend(BeautifulSoup(str(i),'html.parser').find('date'))
#         print('게시일 :', date)


        # 읽기 권한(authority) 파싱
        temp = []
        authoritys = soup.findAll('authority')
        for i in authoritys:
            temp.extend(BeautifulSoup(str(i),'html.parser').find('authority'))
        for i in temp:
            a = i.split(',')
            authority.append(a)
#         print('읽기 권한 :', authority)

        # 제목(title) 파싱
        titles = soup.findAll('title')
        for i in titles:
#             title.extend(BeautifulSoup(str(i),'html.parser').find('title'))
            title.append(i.text)
#         print('타이틀 :', title)



        # 내용(main) 파싱
        temp = []
        mains = soup.findAll('main')
        for i in mains:
            temp.extend(BeautifulSoup(str(i),'html.parser').find('main'))
        for i in temp:
#             a = i.replace('\\n','\n').split('\n')
            a = i.split('@tab@')
            main.append(a)
#         print('메인 :', main)


        # 좋아요수, 댓글 수 (addition) 파싱
        additions = soup.findAll('addition')
        for i in additions:
            addition.extend(BeautifulSoup(str(i),'html.parser').find('addition'))
#         print('좋아요 :', addition)

        # 댓글(comment) 파싱
        comments = soup.findAll('comment')
        temp = []
        for i in comments:
            temp.extend(BeautifulSoup(str(i),'html.parser').find('comment'))
        for i in temp:
            a = i.split('@tab@')
            comment.append(a)
#         print('댓글 :', comment)

        for i in addition :
            # 좋아요 수
            temp_good = re.search('좋아요: (\d+),', str(i), re.I|re.S)
            num_good.append(int(temp_good.group(1)))

            # 댓글 수
            temp_comment = re.search('댓글: (\d+)', str(i), re.I|re.S)
            num_comment.append(int(temp_comment.group(1)))

        # 메모장에서 긁어온 값 전역 변수에 저장
        text_timeline = tmp



class SNS:
    def __init__(self, class_, ID, PWD, name, age, nickname, birth, friend):
        self.class_ = class_
        self.ID = ID
        self.PWD = PWD
        self.name = name
        self.age = age
        self.nickname = nickname
        self.birth = birth
        self.friend = friend

    # 개인정보 및 친구목록 업데이트하기
    def update_friend_info(self):
        with open('./members/member{}.txt'.format(0), 'w',
          encoding='utf-8') as f:
            f.write('<class>' + self.class_ + '</class>\n')
            f.write('<id>' + self.ID + '</id>\n')
            f.write('<pwd>' + self.PWD + '</pwd>\n')
            f.write('<name>' + self.name + '</name>\n')
            f.write('<age>' + self.age + '</age>\n')
            f.write('<nickname>' + self.nickname + '</nickname>\n')
            f.write('<birth>' + self.birth + '</birth>\n')
            f.write('<friend>' + self.friend + '</friend>\n')

    def update_posts(self):
        loading_posts()

    def show_info(self):
        print('#### 정보 ####')
        print('     ID     :', self.ID)
        print('1. 비밀번호  :', self.PWD)
        print('2.   이름   :', self.name)
        print('3.   나이   :', self.age)
        print('4.  닉네임  :', self.nickname)
        print('5.   생일   :', self.birth)
        print('6.  친구목록 \n:', self.friend)

    # 회원정보 변경
    def revise_info(self):
        print('#### 정보 ####')
        print('     ID     :', self.ID)
        print('1. 비밀번호  :', self.PWD)
        print('2.   이름   :', self.name)
        print('3.   나이   :', self.age)
        print('4.  닉네임  :', self.nickname)
        print('5.   생일   :', self.birth)
        print('#############\n')
        print('==== 변경할 번호를 입력하세요. ====')
        input_ = int(input('>>  '))
        if input_ == 1 :
            self.PWD = input('변경할 비밀번호 입력 :')
        elif input_ == 2 :
            self.name = input('변경할 이름 입력 :')
        elif input_ == 3 :
            self.age = input('변경할 나이 입력 :')
        elif input_ == 4 :
            self.nickname = input('변경할 닉네임 입력 :')
        elif input_ == 5 :
            self.birth = input('변경할 생년월일 입력 :')
        else :
            print('잘못된 입력입니다.')

        self.update_friend_info()

    # 친구추가/삭제 하기
    def new_friend(self):
        global id_
        print('1. 친구추가 하기')
        print('2. 친구삭제 하기')
        input__ = int(input('\n>> '))
        if input__ == 1 :
            new_friend = input('친구 ID 입력 \n  >>  ')
            if new_friend in id_ : # 총 id(전역변수)
                self.friend = self.friend + ',' + new_friend
                print('친구 추가가 완료 되었습니다.')
                self.update_friend_info()
            else :
                print('존재하지 않는 ID 입니다.')


    # 게시물(타임라인) 등록
    def write_timeline(self):
        global total_posts
        new_title = input('title : ')
        new_main = input('main :')
        # 게시물 수 하나 증가
        total_posts += 1

        with open('temp.txt','w', encoding='utf-8') as f2:
            global text_timeline
            for i in text_timeline[0:-1]:
                f2.write(i) # 여태 있던 게시물 전부 쓰기

            # 새로운 게시물 쓰기
            f2.write('<post{}>\n'.format(total_posts-1))
            f2.write('<writer>' + self.ID + '</writer>\n')
            f2.write('<date>' + datetime.today().strftime("%Y-%m-%d %H:%M:%S") +
                     '</date>\n')
            f2.write('<authority>' + self.ID + ',' + self.friend + '</authority>\n')
            f2.write('<title>' + new_title + '</title>\n')
            f2.write('<main>' + new_main + '</main>\n')
            f2.write('<addition>좋아요: 0, 댓글: 0</addition>\n')
            f2.write('<comment> </comment>\n')
            f2.write('</post{}>\n\n'.format(total_posts-1))
            f2.write('@@total_posts@@'+str(total_posts)+'@@total_posts@@\n')
        self.update_posts()

    # 게시물 출력
    def show_posts(self) :
        for i in range(total_posts-1, -1, -1):
            if self.ID in authority[i]:
                print('='*60)
                print('Title :', title[i])
                print('게시자 : ' + writer[i] + '   ' + '게시일 : ' + date[i])
                print()
                for j in main[i]:
                    print(j)
                print()
                print(addition[i])
                for j in comment[i]:
                    print(j)
                print('='*60)
                print('\n\n')

    # 게시물 삭제
    def delete_post(self):
        global total_posts
        rr = []
        post = []
        aa = str()
        number = 0
        for i in range(total_posts):
            if self.ID == writer[i]:
                print('{} Title :'.format(i), title[i])
                print()
                print(addition[i])
                number += 1
                print('\n')
        if number != 0:
            input_ = int(input('삭제할 게시물 번호를 입력하세요 >> '))
            if input_ < total_posts:
                with open('temp.txt', 'r', encoding = 'utf-8') as f:
                    rr = f.read()

                    # post에 해당하는 부분 파싱
                    soup = BeautifulSoup(str(rr), 'html.parser')
                    posts = soup.findAll('post{}'.format(input_))

#                     print('post{}'.format(input_), posts)
#                     print()
#                     print('게시물 :', str(posts).replace('[','').replace(']',''))

            #   게시물 삭제
                with open('temp.txt', 'w', encoding = 'utf-8') as f:
                    f.write(rr.replace(str(posts).replace('[','').replace(']',''),
                                       '').replace('@@total_posts@@{}@@total_posts@@'.format(total_posts),''))
                    total_posts -= 1
                    f.write('@@total_posts@@'+str(total_posts)+'@@total_posts@@\n')

                loading_posts()
            else :
                print('게시물이 존재하지 않습니다.')
        else:
            print('등록한 게시물이 없습니다.')

    # 댓글 달기, 댓글 수 업그레이드 (메모장 기능 X)
    def add_comment(self):
        for i in range(total_posts):
            if self.ID in authority[i]:
                print('='*30 + '  {}  '.format(i) + '='*30)
                print('Title :', title[i])
                for j in main[i]:
                    print(j)
                print()
                print(addition[i])
                for j in comment[i]:
                    print(j)
                print('='*62)
                print('\n')
        input_ = input('댓글을 남기고 싶은 타임라임 번호를 선택하세요.\n>> ')
        print('{}'.format(input_) + ' 게시물 선택하였습니다.')
        new_comment = input('>> ')
        comment[int(input_)].append(self.ID + ' : ' + new_comment)
        num_comment[int(input_)] += 1
        addition[int(input_)] = str("좋아요: " + str(num_good[int(input_)]) +
                                    ', 댓글: ' + str(num_comment[int(input_)]))
        print('댓글이 등록 되었습니다.')

    # 좋아요 누르기, 좋아요 수 업그레이드 (메모장 기능 X)
    def add_good(self):
        for i in range(total_posts):
            if self.ID in authority[i]:
                print('='*30 + '  {}  '.format(i) + '='*30)
                print('Title :', title[i])
                for j in main[i]:
                    print(j)
                print()
                print(addition[i])
                for j in comment[i]:
                    print(j)
                print('='*62)
                print('\n')
        input_ = input('좋아요를 누를 게시물 번호를 입력하세요.\n>> ')
        print('{}'.format(input_) + ' 게시물 선택하였습니다.')
        num_good[int(input_)] += 1
        addition[int(input_)] = str("좋아요: " + str(num_good[int(input_)]) + ', 댓글: '
                                    + str(num_comment[int(input_)]))

        print('좋아요를 눌렀습니다.')

    def friend_info(self):
        global id_
        num = 1
        print('########## 친구 목록 ##########')
        for i in friend[int(self.class_)].split(','):
            print('{}. {}'.format(num, i))
            for j in range(len(id_)):
                if i == id_[j] :
                    print('이름 : {}'.format(name[j]))
                    print('생일 : {}'.format(birth[j]))
                    print('닉네임 : {}'.format(nickname[j]))
                    print()
            num += 1

    # 메뉴출력
    # 로그인 성공시 화면
    # 메뉴출력하면서, 타임라인이 보여야함.
    def options(self):
        print('\n\n')
        print(' '*15+'###################')
        print(' '*15+'#1. 타임라인 등록  #')
        print(' '*15+'#2. 좋아요 누르기  #')
        print(' '*15+'#3.  댓글 달기    #')
        print(' '*15+'#4. 타임라인 삭제  #')
        print(' '*15+'#5.  친구 추가    #')
        print(' '*15+'#6.  친구 목록    #')
        print(' '*15+'#7. 좋아요 누르기  #')
        print(' '*15+'#8.  회원 정보    #')
        print(' '*15+'#9.  로그 아웃    #')
        print(' '*15+'###################')
        input_ = int(input('>> '))

        if input_ == 1:
            self.write_timeline()
            self.show_posts()
        elif input_ == 2:
            self.add_good()
            self.show_posts()
        elif input_ == 3:
            self.add_comment()
            self.show_posts()
        elif input_ == 4:
            self.delete_post()
            self.show_posts()
        elif input_ == 5:
            self.new_friend()
        elif input_ == 6:
            self.friend_info()
        elif input_ == 7:
            self.add_good()
            self.show_posts()
        elif input_ == 8:
            self.show_info()
        elif input_ == 9:
            member = 0
            return -1


# main
loading()
loading_posts()


# 초기 화면
while True:
    loading()
    loading_posts()
    print('\n\n\n\n\n\n\n\n')
    print('#################')
    print('#1.    login    #')
    print('#2. assginment  #')
    print('#################')
    print()
    input_ = int(input('>> '))
    if input_ == 1 :
        account_number = login()
        if account_number != -1 :
            member = SNS(class_[account_number], id_[account_number],
             pwd[account_number], name[account_number],
                age[account_number], nickname[account_number],
                birth[account_number], friend[account_number])
            member.show_posts()
            while True:
                print()
                flag = 0
                flag = member.options()
                if flag == -1 :
                    break

        elif account_number == -1 :
            print('\n비밀 번호를 5번 이상 틀려,\n초기 화면으로 돌아갑니다.')
    elif input_ == 2 :
        assignment()
    else :
        print('잘못된 입력입니다.')
