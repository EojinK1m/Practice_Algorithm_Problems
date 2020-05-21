#https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A.pop() * B.pop()

    return answer

