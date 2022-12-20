"""
string 형 배열 seoul의 element중 "Kim"의 위치를 찾아,
"김서방은 x에 있다"는 string을 반환하는 함수, solution을 완성하세요
seoul에 "Kim"은 오직 한번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한사항
- seoul은 길이 1이상, 1000 이하인 배열
- seoul의 우너소는 길이 1이상, 20이하인 문자열
- kim은 반드시 seoul 안에 포함되어있습니다.
"""
def solution(seoul):
    answer='김서방은 {}에 있다'.format(seoul.index("Kim"))
    return answer

print(solution(["f", "Kim"]))