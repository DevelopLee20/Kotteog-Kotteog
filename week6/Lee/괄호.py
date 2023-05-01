def solution():
    stack = []

    for i in [i for i in input()]:
        if i == '(':
            stack = stack + [i]
        else:
            if len(stack):
                stack = stack[:-1]
            else:
                return "NO"
    
    if len(stack):
        return "NO"
    return "YES"

for _ in range(int(input())):
    print(solution())