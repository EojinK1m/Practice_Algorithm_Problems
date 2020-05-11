#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    blocks = [0] * N
    reaches = [0] * N

    for stage in stages:
        for i in range(stage):
            if(i >= N): continue

            reaches[i] += 1
        if not stage > N:
            blocks[stage -1] += 1

    fail_p = []

    for i in range(N):
        fail_p.append([ i +1])
        try:
            fail_p[i].append(blocks[i] / reaches[i])
        except ZeroDivisionError:
            fail_p[i].append(0)


    fail_p = sorted(fail_p, key=lambda f: f[1], reverse = True)
    return [i[0] for i in fail_p]