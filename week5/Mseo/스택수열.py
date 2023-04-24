#스택수열
"""
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
"""
import sys
I=sys.stdin.readline
class stack:
    #초기화
    def __init__(self):
        #빈배열을 생성
        self.array=[]
    #정수를 스택에 넣는다
    def push(self,item):
        self.array.append(item)
    #스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다
    #만약 스택에 들어있는 정수가 없을 경우에는 -1을 출력한다
    def pop(self):
        #스택이 비어있다면 -1을 출력
        if(self.isEmpty()):
            print(-1)
        #아니라면 꺼낸 값을 출력
        else:
            print(self.array.pop())
    #스택에 들어있는 정수의 개수를 출력한다
    def size(self):
        return len(self.array)
    #스택이 비어있으면 1, 아니면 0을 출력
    def isEmpty(self):
        #스택이 비어있으면 1
        if(len(self.array)==0):
            return 1
        #스택이 비어있지 않으면 0
        else:
            return 0
    def top(self):
        #만약 스택이 비어있다면 -1을 출력
        if(self.isEmpty()):
            print(-1)
        #아니라면 스택의 가장 위에 있는 정수를 출력한다
        else:
            print(self.array[-1])

#입력_ 첫째 줄에 주어지는 명령의 수 N이 주어진다

N=int(I())
stack_=stack()