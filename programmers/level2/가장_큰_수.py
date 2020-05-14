#https://programmers.co.kr/learn/courses/30/lessons/42746#


def solution(numbers):
    max_length = len(str(max(numbers)))
    numbers = [str(n) for n in numbers]

    list_for_sort = [[n, n + n[0] * (max_length - len(n)), len(n) * (int(n[-1]) - int(n[0]))] for n in numbers]

    list_for_sort.sort(key=lambda n: (int(n[1]), n[2]), reverse=True)

    answer = ''
    for i in list_for_sort:
        if answer == '0':
            if not i[0] == '0':
                answer = ''
            else:
                continue
        answer += i[0]

    return answer