# 민서몬 도와줘!!!

def push_front(deque:list, X:int):
    deque = [X] + deque

def push_back(deque:list, X:int):
    print(X)
    print(deque)
    deque = deque + [X]

def pop_front(deque:list):
    if empty(deque):
       return -1
    temp = deque[0]
    deque = deque[:1]
    return temp

def pop_back(deque:list):
    if empty(deque):
        return -1
    temp = deque[-1]
    deque = deque[:-1]
    return temp

def size(deque:list):
    return len(deque)

def empty(deque:list):
    return (size(deque) == 0)

def front(deque:list):
    if empty(deque):
        return -1
    return deque[0]

def back(deque:list):
    if empty(deque):
        return -1
    return deque[-1]

import sys

deque = []

for _ in range(int(input())):
    orders = list(sys.stdin.readline().split(" "))

    if len(orders) == 1:
        exec(f"print({orders[0]}(deque))")
    else:
        exec(f"print({orders[0]}(deque, {int(orders[1])}))")
        print(push_back(deque, 1))

    print(deque)