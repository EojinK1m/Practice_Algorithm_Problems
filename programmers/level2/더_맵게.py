#https://programmers.co.kr/learn/courses/30/lessons/42626#

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+ heapq.heappop(scoville)*2)
            answer += 1
        except:
            return -1
    return answer