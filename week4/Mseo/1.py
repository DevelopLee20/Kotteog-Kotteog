#완주하지 못한 선수
"""
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한명의 선수를 제외하고는
모든 선수가 마라톤을 완주하였습니다

마라톤에 참여한 선수들의 이름이 담긴 배열과 완주한 선수들의 이름이 담긴 배열이 주어질 때
완주하지 못한 선수의 이름을 리턴하세요

주의: 동명이인이 있을 수 있다 -> 어떻게 코드를 짜야 효율적일까...?

[i for i in paticipant if i not in completion][0]
-> 이 코드는 중복을 해결할 수 없음

-> for if 같이 쓰는 숏코딩

-> 해시를 사용하는 문제
"""
#참여한 선수 들, 완주한 선수들
def solution(participant, completion):
    for i in participant:
        if i not in completion:
            return i
        completion.remove(i)