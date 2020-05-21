#https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    map = {}

    for r in record:
        t = r.split()
        if t[0] == 'Leave':
            continue
        else:
            map[t[1]] = t[2]

    for r in record:
        t = r.split()
        if t[0] == 'Change':
            continue
        elif t[0] == 'Enter':
            answer.append(map[t[1] ] +"님이 들어왔습니다.")
        else:
            answer.append(map[t[1] ] +"님이 나갔습니다.")

    return answer