#https://programmers.co.kr/learn/courses/30/lessons/12940

# 유클리드 호제법 사용
# 참고
# http://lonpeach.com/2017/11/12/Euclidean-algorithm/
def solution(n, m):
    temp_n, temp_m = n, m
    answer = []

    while (temp_m > 0):
        temp = temp_n
        temp_n = temp_m
        temp_m = temp % temp_n

    answer.append(temp_n)
    answer.append(n * m // temp_n)
    return answer