#https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    s = list(s)
    stack = [s.pop()]

    while s:
        a = s.pop()
        if not stack or not stack[-1] == a:
            stack.append(a)
        else:
            stack.pop()

    if stack:
        return 0
    else:
        return 1