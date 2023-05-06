# 괄호가 잘못된 경우 예외처리가 안됨 ㅠ

def push(stack:list, num:int):
    # 왜 안될까?
    # stack = stack + [num]
    stack.append(num)
    
def pop(stack:list):
    # 왜 안될까?
    # num = stack[-1]
    # stack = stack[:-1]
    if isEmpty(stack):
        return -1
    return stack.pop()

def isEmpty(stack:list):
    return (len(stack) == 0)

def solution():
    stack = []
    count1 = 0; count2 = 0

    for i in input():
        if i in ['(','[']:
            count1 += 1
            push(stack, i)
        
        else:
            count2 += 1
            summ = 0
            temp = pop(stack)
            
            if pop == -1:
                return 0
            
            while temp != '(' and temp != '[':
                summ += int(temp)
                temp = pop(stack)
                
                if pop == -1:
                    return 0
            
            if temp == '(':
                if summ:
                    push(stack, 2*summ)
                else:
                    push(stack, 2)
            else:
                if summ:
                    push(stack, 3*summ)
                else:
                    push(stack, 3)
                    
    return sum(stack)

print(solution())