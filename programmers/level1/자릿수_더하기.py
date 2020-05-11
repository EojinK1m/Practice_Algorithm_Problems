#https://programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer