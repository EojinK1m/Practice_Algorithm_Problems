#https://programmers.co.kr/learn/courses/30/lessons/42586

import math


def solution(progresses, speeds):
    # first
    #     progresses.reverse()
    #     speeds.reverse()
    #     answer = []
    #     while(progresses):
    #         num_of_clear_progresses = 0
    #         try:
    #             while(progresses[-1] >= 100):
    #                 progresses.pop()
    #                 speeds.pop()
    #                 num_of_clear_progresses += 1
    #         except IndexError:
    #             answer.append(num_of_clear_progresses)
    #             break

    #         if(num_of_clear_progresses):
    #             answer.append(num_of_clear_progresses)

    #         for i in range(len(progresses)):
    #             progresses[i] += speeds[i]
    #   return answer
    Q = []
    for p, s in zip(progresses, speeds):
        day_for_clear = math.ceil(-(p - 100) / s)
        if (not Q or Q[-1][1] < day_for_clear):
            Q.append([1, day_for_clear])
        else:
            Q[-1][0] += 1

    return [q[0] for q in Q]