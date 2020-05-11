#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    st = []

    for s in range(n):
        st.append(0)
        if s + 1 in lost:
            st[s] -= 1
        if s + 1 in reserve:
            st[s] += 1

    reserve = [s for s in range(n) if st[s] == 1]

    for r in reserve:
        f = r + 1
        b = r - 1

        if not r == 0:
            if st[b] == -1:
                st[b] = 0
                st[r] = 0
                continue
        if not r + 1 == n:
            if st[f] == -1:
                st[f] = 0
                st[r] = 0

    answer = n - st.count(-1)
    return answer