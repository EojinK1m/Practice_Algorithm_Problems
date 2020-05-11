#https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    arr.reverse()
    answer = []
    while arr:
        t = arr.pop()
        if not answer or answer[-1] != t: answer.append(t)

    return answer