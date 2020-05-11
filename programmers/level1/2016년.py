#https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    for month in range(1, a):
        w = 0
        if month >= 8:
            w += 1
        if month == 2:
            b += 29
        elif month % 2 == w:
            b += 30
        else:
            b += 31

    b -= 1
    b = b % 7

    answer = days[b]

    return answer