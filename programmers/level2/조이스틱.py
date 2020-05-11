#https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    make_name = 'A' * len(name)
    make_index = 0
    A2num = ord('A')

    name_copy = name
    while (True):
        if (name[make_index] != make_name[make_index]):
            temp = ord(name[make_index]) - A2num
            if (temp > 13):
                temp = 26 - temp
            answer += temp
            make_name = make_name[0:make_index] + name[make_index] + make_name[make_index + 1:]

        if (name == make_name):
            break

        forward_distance = 0
        temp_index_f = make_index
        while (True):
            temp_index_f += 1
            if (temp_index_f >= len(name)):
                temp_index_f = 0
            forward_distance += 1
            if (name[temp_index_f] != make_name[temp_index_f]):
                break

        backward_distance = 0
        temp_index_b = make_index
        while (True):
            temp_index_b -= 1
            if (temp_index_b < 0):
                temp_index_b = len(name) - 1
            backward_distance += 1
            if (name[temp_index_b] != make_name[temp_index_b]):
                break

        if (forward_distance <= backward_distance):
            make_index = temp_index_f
            answer += forward_distance
        else:
            make_index = temp_index_b
            answer += backward_distance

    return answer