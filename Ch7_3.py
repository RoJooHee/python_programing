#push x : 정수x 큐에 넣기 / pop : 큐 가장 앞에있는 정수 빼고 그 수 출력. 비어있으면 -1
#size : 큐에 든 정수 개수 출력 / empty : 비어있으면 1 아니면 0 출력
#front : 큐 가장 앞의 정수 출력. 비어있으면 -1 / back : 큐 가장 뒤의 정수 출력. 비어있으면 -1
#첫줄에는 1~100000 주어지는 명령 개수
a=int(input("입력할 명령 개수를 입력하세요 : "))
while (a>100000 or a<1) : a=int(input("입력할 명령 개수 1~100000 사이로 입력하세요 : "))

def pop():
    if len(queue)==0 : return -1
    item=queue[0] #return을 위해 뺄 값을 미리 저장해두고
    del queue[0] #가장 앞에 있는 정수를 뺌
    return item

def empty():
    if len(queue)==0 : return 1
    else : return 0

def front():
    if len(queue)==0 : return -1
    else : return queue[0] #가장 앞의 정수 출력

def back():
    if len(queue)==0 : return -1
    else : return queue[-1] #가장 뒤의 정수 출력

queue=[]

for i in range(a) :
    say=input("명령 입력하세요 : ").split()
    if say[0]=="push" :
        queue.append(say[1]) #push할 값은 공백으로 나뉘어진 say[1]임
    elif say[0]=="pop" :
        print(pop())
    elif say[0]=="size" :
        print(len(queue)) #size는 queue의 길이를 통해 구함
    elif say[0]=="empty" :
        print(empty())
    elif say[0]=="front" :
        print(front())
    elif say[0]=="back" :
        print(back())
    else : print("") #예외처리
