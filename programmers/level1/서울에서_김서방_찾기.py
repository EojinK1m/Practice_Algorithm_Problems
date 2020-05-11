#https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = ''
    for i, n in enumerate(seoul):
        if n == 'Kim':
            return f'김서방은 {i}에 있다'