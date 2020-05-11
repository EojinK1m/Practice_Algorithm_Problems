#https://programmers.co.kr/learn/courses/30/lessons/12921

import math
def solution(n):
    sieve = [True ] *( n +1)

    for i in range(2, n+ 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return sieve.count(True) - 2