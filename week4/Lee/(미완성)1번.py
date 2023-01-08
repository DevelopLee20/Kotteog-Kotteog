# 정확성 100, 효율성 0
# 원인 분석 : 일단은 모르겠음;;
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]