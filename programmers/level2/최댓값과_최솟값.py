#https://programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    s = [int(i) for i in s.split()]
    return f'{min(s)} {max(s)}'