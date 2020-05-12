#https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0

    index = 0
    first_priority = 0
    while True:
        if not first_priority:
            first_priority = max(priorities)

        while True:
            if (first_priority == priorities[index]):
                priorities[index] = 0
                first_priority = 0
                answer += 1
                break
            index += 1
            if (index == len(priorities)):
                index = 0

        if (index == location):
            break

    return answer