#https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

a = '*'*a
a += '\n'
a *= b
print(a)