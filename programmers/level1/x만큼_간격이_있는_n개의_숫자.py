#https://programmers.co.kr/learn/courses/30/lessons/12954#

def solution(x, n):
    if x == 0:
        return [0]*n
    elif x < 0:
        a = -1
    else:
        a = 1
    return [i for i in range(x, n*x+a, x)]