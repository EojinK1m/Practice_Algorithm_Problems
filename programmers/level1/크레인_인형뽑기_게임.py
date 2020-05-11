#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    deep_of_board = len(board)
    basket = []

    for now_move in moves:
        now_move -= 1

        for now_deep in range(deep_of_board):
            if board[now_deep][now_move]:
                basket.append(board[now_deep][now_move])
                board[now_deep][now_move] = 0

                if (len(basket) >= 2):
                    basket_pop_1 = basket.pop()
                    basket_pop_2 = basket.pop()
                    if not basket_pop_1 == basket_pop_2:
                        basket.append(basket_pop_2)
                        basket.append(basket_pop_1)
                    else:
                        answer += 2
                break

    return answer