#https://programmers.co.kr/learn/courses/30/lessons/17682


def solution(dart_result):
    dart_result = list(dart_result)
    dart_result.reverse()
    score = list()

    while(dart_result):
        print(dart_result)
        r = dart_result.pop()
        if(r.isdigit()):
            if(dart_result[-1:][0].isdigit()):
                num = int( r +dart_result.pop())
            else:
                num = int(r)
            score.append(num)

        elif(r.isalpha()):
            if r == 'S':
                power = 1
            elif r == 'D':
                power = 2
            else:
                power = 3
            o = score[-1]
            for i in range(1, power):
                score[-1] *= o
        else:
            if r == '#':
                score[-1] *= -1
            else:
                if len(score)>=2:
                    score[-2] *= 2
                score[-1] *= 2
        print(score)
    answer = 0
    print(score)
    for s in score:
        answer += s
    return answer