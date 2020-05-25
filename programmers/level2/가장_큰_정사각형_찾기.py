#https://programmers.co.kr/learn/courses/30/lessons/12905#

def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue

            board[i][j] += min([board[i - 1][j],
                                board[i - 1][j - 1],
                                board[i][j - 1]])

    for b in board:
        for n in b:
            if n > answer:
                answer = n

    return answer ** 2