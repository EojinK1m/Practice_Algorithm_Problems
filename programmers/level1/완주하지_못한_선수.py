#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    hash_table = dict()

    for p in completion:
        hashed_p = hash(p)

        if hashed_p in hash_table:
            hash_table[hashed_p] += 1
        else:
            hash_table[hashed_p] = 1

    for c in participant:
        hashed_c = hash(c)

        if hashed_c in hash_table:
            if hash_table[hashed_c] >= 1:
                hash_table[hashed_c] -= 1
                continue
        answer = c
        break

    return answer