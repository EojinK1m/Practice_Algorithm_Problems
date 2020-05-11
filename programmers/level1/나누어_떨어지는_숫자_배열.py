#https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer