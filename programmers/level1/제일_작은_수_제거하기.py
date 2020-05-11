#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if(len(arr) == 1):
        return [-1]
    s = arr[0]
    for i in arr:
        if i < s:
            s = i
    del arr[arr.index(s)]
    return arr