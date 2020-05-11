#https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    return s.count('p')+s.count('P') == s.count('y')+s.count('Y')