#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        s_array = array[command[0]-1:command[1]]
        s_array.sort()
        answer.append(s_array[command[2]-1])
    return answer