#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    a = 0
    citations.sort(reverse=True)
    for i in range(len(citations ) +1):
        t = 0
        for c in citations:
            if i <=  c:
                t += 1
        if t >= i and i > a:
            a = i

    return a
