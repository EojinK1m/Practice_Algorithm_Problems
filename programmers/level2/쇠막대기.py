#https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    answer = 0
    bar = 0
    bar_c = 0

    for m in range(len(arrangement)):
        if arrangement[m] == '(':
            bar += 1
        else:
            if arrangement[m - 1] == '(':
                bar -= 1
                answer += bar * 2 + bar_c
                bar_c += bar
                bar = 0
            else:
                if bar_c:
                    bar_c -= 1
                else:
                    bar -= 1

    return answer