#https://programmers.co.kr/learn/courses/30/lessons/12949

#선형대수의 행렬의 곱이 어떻게 되는지 알아야 풀 수 있당

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            s = 0
            for l in range(len(arr2)):
                s += arr1[i][l] * arr2[l][j]
            answer[i].append(s)
    return answer