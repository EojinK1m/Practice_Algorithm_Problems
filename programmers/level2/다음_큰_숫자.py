#https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    n_of_one = bin(n).count('1')
    t = n
    while True:
        t += 1
        if n_of_one == bin(t).count('1'):
            return t