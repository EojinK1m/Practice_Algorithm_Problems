#https://programmers.co.kr/learn/courses/30/lessons/60058

def is_correct_string(str):
    temp = 0
    for c in str:
        if c == '(':
            temp += 1
        else:
            if temp > 0:
                temp -= 1
    return not temp

def devide2uv(str):
    stack = 0
    i = 0

    for i in range(len(str)):
        if str[i] == '(':
            stack += 1
        else:
            stack -= 1
        if i% 2 != 0:
            if stack == 0:
                break

    return str[0:i + 1], str[i + 1:]


def solution(w):
    u, v = devide2uv(w)
    if is_correct_string(u):
        v = solution(v)
        return u + v
    else:
        temp = '(' + solution(v) + ')'
        u = [')' if i == '(' else '(' for i in u[1:-1]]
        return temp + ''.join(u)