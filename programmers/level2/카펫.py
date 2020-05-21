#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for h in range(1, yellow + 1):
        if not yellow % h == 0:
            continue

        if (yellow // h * 2) + (h * 2) + 4 == brown:
            return [yellow // h + 2, h + 2]
