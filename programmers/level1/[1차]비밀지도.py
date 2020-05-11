#https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = list()

    for i in range(n):
        arr1[i] = ('{0:0>' + str(n) + 'b}').format(arr1[i])
        arr2[i] = ('{0:0>' + str(n) + 'b}').format(arr2[i])
        temp = ''
        for j in range(n):
            if int(arr1[i][j]) or int(arr2[i][j]):
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer