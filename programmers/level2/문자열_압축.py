#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if (len(s) == 1): return 1
    answer = 0

    for i in range(1, len(s) // 2 + 1):
        split_s = []
        result_s = ''
        for j in range(0, len(s) - 1, i):
            split_s.append(s[j:j + i])
        if s[j + i:]:
            split_s.append(s[j + i:])

        num_of_same = 0
        same = ''

        for j in split_s:

            if not same:
                same = j
            elif same == j:
                num_of_same += 1
            else:
                if num_of_same:
                    result_s += str(num_of_same + 1)
                result_s += same
                same = j
                num_of_same = 0

        if num_of_same:
            result_s += str(num_of_same + 1)
        result_s += same

        if not answer or len(result_s) < answer:
            answer = len(result_s)

    return answer