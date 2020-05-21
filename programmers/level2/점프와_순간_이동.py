#https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    using_battery = 0

    while n:
        if not n % 2 == 0:
            using_battery += 1
            n -= 1
        else:
            n //= 2

    return using_battery