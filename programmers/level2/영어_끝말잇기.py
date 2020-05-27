#https://programmers.co.kr/learn/courses/30/lessons/12981


import math

def solution(n, words):
    history = {}
    for index, word in enumerate(words):
        if index == 0:
            pass
        elif word[0] != words[index - 1][-1]:
            break
        try:
            if history[word] == 1:
                break
        except:
            history[word] = 1
    else:
        return [0, 0]

    user = (index + 1) % n
    if user == 0:
        user = n
    return [user, math.ceil((index + 1) / n)]