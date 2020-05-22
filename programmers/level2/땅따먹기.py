#https://programmers.co.kr/learn/courses/30/lessons/12913#


import sys
sys.setrecursionlimit(1000000)
#재귀 깊이 제한때문에 통과가 안됐음;;

def solution(land, h = -1, w = 0, history = {}):

    try:
        return  history[(h, w)]
    except KeyError:
        pass

    if h == len(land)-1:
        history[(h, w)] = land[h][w]
    else:
        r = 0
        for i in range(4):
            t = solution(land, h+1, i, history)

            if h == -1:
                if t > r:
                    r = t
                    history[(h, w)] = t
            else:
                if i == w:
                    continue
                if t > r:
                    r = t
                    history[(h, w)] = t + land[h][w]

    return history[(h, w)]

