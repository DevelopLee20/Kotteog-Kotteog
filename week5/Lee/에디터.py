import sys

input = sys.stdin.readline

stack = [i for i in input()]
stack = stack[:-1]
temp_stack = []

def push(stack:list, num:int):
    stack.append(num)

def pop(stack:list):
    return stack.pop()

for _ in range(int(input())):
    order = input()

    if order[0] == 'L':
        if len(stack):
            push(temp_stack, pop(stack))

    elif order[0] == 'D':
        if len(temp_stack):
            push(stack, pop(temp_stack))
    
    elif order[0] == 'B':
        if len(stack):
            pop(stack)
    
    else:
        push(stack, order[2])

for i in stack+temp_stack[::-1]:
    print(i, end="")