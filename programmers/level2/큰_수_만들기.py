#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    s = 0
    for i in range(k):
        for j in range(s, len(number) - 1):
            if number[j] < number[j + 1]:
                number = number[:j] + number[j + 1:]
                if (j != 0):
                    s = j - 1
                break
        else:
            number = number[:-1]

    return number