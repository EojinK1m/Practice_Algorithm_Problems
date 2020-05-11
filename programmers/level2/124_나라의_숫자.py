#https://programmers.co.kr/learn/courses/30/lessons/12899


def solution(n):
    answer = ''

    while (n):
        remainder = n % 3
        n //= 3
        if (remainder == 0):
            answer += '4'
            n -= 1
        else:
            answer += f'{remainder}'

    return answer[::-1]