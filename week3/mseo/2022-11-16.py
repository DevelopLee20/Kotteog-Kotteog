"""
어떤 정수들이 있습니다.
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와
이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다
실제 정수들의 합을 구하여 return하도록 solution 함수를
완성해주세요

참이면 양수고 거짓이면 음수이다
"""
def solution(absolutes, signs):
    a=0
    for i in range(len(absolutes)):
        a=eval("a{}{}".format( "+" if signs[i]==True else "-",absolutes[i]))
    return a

print(solution([4,7,12],[True,False,True]))

"""
print(exec("a=a{}{}".format(signs[i],absolutes[i]))
이건 왜 안돌아갈까?

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

"""