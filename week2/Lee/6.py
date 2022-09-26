def solution(num):
    for i in range(500):
        if num == 1:
            return i
        
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
            
    return -1