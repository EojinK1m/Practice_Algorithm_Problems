#https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    hz = True

    for i in s:
        if i == ' ':
            hz = True
            answer += ' '
        else:
            if hz:
                answer += i.upper()
                hz = False
            else:
                answer += i.lower()
                hz = True

    return answer