#https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings:strings[n])