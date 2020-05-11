#https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, num):
    answer = ''
    for i in s:
        n = num
        if i.isalpha():
            a = ord(i)
            if a < ord('a'):
                l = ord('Z')
            else:
                l = ord('z')

            while (True):
                if a + n > l:
                    n -= l - a + 1
                    a = l - 25
                else:
                    a += n
                    answer += chr(a)

                    break
        else:
            answer += ' '
    return answer