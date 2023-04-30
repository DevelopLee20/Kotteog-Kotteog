# 아직 못함;;

import sys

# input = sys.stdin.readline

def pop(stack:list, output:list):
    stack = stack[:1]
    output = output + ['-']

def push(stack:list, output:list, num:int):
    stack = stack + [num]
    output = output + ['+']

def solution():
    num = int(input())
    stack = []
    array = []
    output = []
    idx = 0

    for _ in range(num):
        array = array + [int(input())]

    push(stack, output, 1)
    for i in range(2, num+1):
        if i == array[idx]:
            pop(stack, output)
            idx = idx + 1
        elif i > array[idx]:
            if len(stack): # isempty
                pop(stack, output)
            else:
                return "NO"
        else:
            push(stack, output, i)
            
    return output


print(solution())