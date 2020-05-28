#https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(st):
    s, e = 0, 0

    st = list(st)
    st.reverse()
    while st:
        p = st.pop()

        if p == '(':
            s += 1
        else:
            if s:
                s -= 1
            else:
                e += 1

    return s == 0 and e == 0
