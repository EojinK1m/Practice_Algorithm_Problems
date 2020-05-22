#https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    d = {}

    for i in nums:
        try:
            d[i] += 1
        except KeyError:
            d[i] = 1
    # set을 사용하면 더 간결하게 할 수 있당
    # set(nums)

    answer = len(d.keys())
    if answer > len(nums )//2:
        answer = len(nums )//2


    return answer