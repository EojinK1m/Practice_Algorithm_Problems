#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    ways = {}
    for c in clothes:
        try:
            ways[c[1]] += 1
        except:
            ways[c[1]] = 1

    answer = 1
    for w in ways.values():
        answer *= w + 1
    return answer - 1