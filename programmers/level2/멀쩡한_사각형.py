#https://programmers.co.kr/learn/courses/30/lessons/62048

import math


def solution(w, h):
    if (w == h):
        return w * h - w
    elif (w == 1 or h == 1):
        return 0
    answer = w * h
    one = 0

    gcd = math.gcd(w, h)
    w = int(w / gcd)
    h = int(h / gcd)

    y_1 = 0
    y_2 = 1
    slope = h / w

    for x in range(1, w + 1):
        y_1 = y_2 - 1
        y_2 = math.ceil(x * slope)

        one += y_2 - y_1

    return answer - one * gcd