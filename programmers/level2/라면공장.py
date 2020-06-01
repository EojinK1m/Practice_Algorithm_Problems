#https://programmers.co.kr/learn/courses/30/lessons/42629

import heapq
from collections import deque


def solution(stock, dates, supplies, k):
    answer = 0

    sd = deque(zip(supplies, dates))
    heap = []

    while stock <= k - 1:
        while sd:
            if sd[0][1] <= stock:
                p = sd.popleft()
                heapq.heappush(heap, -p[0])
            else:
                break

        stock -= heapq.heappop(heap)
        answer += 1

    return answer

