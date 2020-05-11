#https://programmers.co.kr/learn/courses/30/lessons/12982


def solution(d, budget):
    answer = 0

    while (d):
        ask_d = min(d)
        d.remove(ask_d)

        if (budget - ask_d < 0):
            break
        else:
            budget -= ask_d
            answer += 1

    return answer