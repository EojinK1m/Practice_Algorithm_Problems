#https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = []

    for _ in range(len(heights)):
        send_h = heights.pop()

        for i in range(len(heights), -1, -1):
            try:
                if(heights[i-1] > send_h):
                    break
            except:
                pass
        answer.append(i)

    answer.reverse()
    return answer