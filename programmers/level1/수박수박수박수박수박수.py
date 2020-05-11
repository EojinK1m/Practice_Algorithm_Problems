#https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    if (n % 2 == 0):
        n //= 2
        answer = '수박' * n
    else:
        answer = '수'
        n = (n - 1) // 2
        answer += '박수' * n

    return answer