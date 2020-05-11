#https://programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return x%sum==0