#https://programmers.co.kr/learn/courses/30/lessons/12903


def solution(s):
    l = len(s)
    return s[(l-1)//2:(l-1)//2+(2-l%2)]