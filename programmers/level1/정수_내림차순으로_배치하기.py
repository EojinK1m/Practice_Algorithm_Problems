#https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))