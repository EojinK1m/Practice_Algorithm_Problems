#https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].replace('},{', ' ').split(' ')
    s.sort(key=len)
    for n, i in enumerate(s):
        s[n] = [int(j) for j in i.split(',')]

    answer = []
    for i in s:
        for j in i:
            if not j in answer:
                answer.append(j)

    return answer