#https://programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    a = math.sqrt(n)
    if (a-int(a) != 0):
        return -1
    else:
        return (int(a)+1) * (int(a)+1)