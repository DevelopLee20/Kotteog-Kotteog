def solution(s):
    sump = 0; sumy = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            sump = sump + 1
        elif i == 'y' or i == 'Y':
            sumy = sumy + 1
            
    return sump == sumy