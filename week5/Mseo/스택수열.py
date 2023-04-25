#스택수열
"""
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

문제를 이해하는데 좀 걸렸다 내가 멍청한건가? 이해하고 보니 간단하단

처음에 숫자 개수 n을 입력받고
1~n 숫자를 차례대로 push pop을 이용하여
사용자로부터 입력받은 수열을 만드는 것이다

그렇다면 수열이 만들어지지 못하는 경우는 어떤 경우일까?
마지막에 스택에 들어가 있는 리스트와 내가 만들어야하는 수열의 나머지가 같지 않다면 수열은 못만드는 것이다

문제 1: 오류
: 틀렸다고 뜨길래 생각해보니
    if(len(stack_)==0):
            stack_.append(i)
            i+=1
            result.append('+')
    if stack_[-1] == sequence[k]:
        #만약 스택이 비어있다면 값을 넣어준다
        stack_.pop()
        result.append('-')
        k+=1
    else:
        stack_.append(i)
        i+=1
        result.append('+')

스택이 비었는지를 확인할때 비어있지않은 경우 else까지 넘어가서 오류가 나는거 같아 나눠주었다
"""
import sys
I=sys.stdin.readline

#입력_ 첫째 줄에 주어지는 명령의 수 N이 주어진다
N=int(I())
stack_=[]
i=1
#사용자로부터 입력받은 수열값을 저장할 배열
sequence=[int(input()) for _ in range(N)]
#위 배열의 인덱스 역할
k=0
#결과를 저장할 배열
result=[]

while(i!=N+1):
    if(len(stack_)==0):
            stack_.append(i)
            i+=1
            result.append('+')
    if stack_[-1] == sequence[k]:
        #만약 스택이 비어있다면 값을 넣어준다
        stack_.pop()
        result.append('-')
        k+=1
    else:
        stack_.append(i)
        i+=1
        result.append('+')

if stack_[:] == sequence[:k-1:-1]:
     for i in result:
        print(i)
     for _ in stack_:
        print('-')
else:
    print("NO")

"""
옛날에 풀어서 맞춘거 1년전의 민서가 더 똑똑한 듯
import sys
I=sys.stdin.readline

#첫 줄에 n이 주어진다
n=int(I())
#n개의 숫자를 입력받는다
list_=list(int(I()) for _ in range(n))
list1_=list(i for i in range(1,n+1))

index_=0
index1_=0
result_=[]
stack_=[0,]

while(index1_!= n):
    if(list_[index_]==stack_[-1]):
        stack_.pop()
        result_.append("-")
        index_+=1
        continue

    stack_.append(list1_[index1_])
    index1_+=1
    result_.append("+")

if(list_[index_:]==stack_[n:0:-1]):
    for i in result_:
        print(i)
    for _ in range(len(stack_)-1):
        print("-")
else:
    print("NO")

"""