#https://programmers.co.kr/learn/courses/30/lessons/12945#


def p(n, f=dict()):
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def solution(n):
    return p(n)%1234567