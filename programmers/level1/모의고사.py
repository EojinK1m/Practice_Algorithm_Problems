#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    number_of_answers = [0, 0, 0]
    answers_of_students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for i in range(len(answers)):
        for j in range(3):
            s_a = answers_of_students[j]
            if s_a[i % len(s_a)] == answers[i]:
                number_of_answers[j] += 1

    b = 0
    for i in number_of_answers:
        if i > b:
            b = i

    for i in range(3):
        if number_of_answers[i] == b:
            answer.append(i + 1)

    return answer