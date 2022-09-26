'''
배운거 : range 자체가 사이값의 리스트를 반환함
'''
def solution(a, b):
    if a > b:
        return sum([i for i in range(b,a+1)])
    elif a < b:
        return sum([i for i in range(a,b+1)])
    else:
        return a