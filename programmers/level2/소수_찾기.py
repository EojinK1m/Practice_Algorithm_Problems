#https://programmers.co.kr/learn/courses/30/lessons/42839

def check_sosu(number):
    if number == 0 or number == 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def func(numbers, adding_str='', history=[]):
    if numbers == []:
        if not adding_str == '':
            num = int(adding_str)
            if (check_sosu(num)):
                if not num in history:
                    history.append(num)
    else:
        for now_number in numbers:
            t_numbers = numbers.copy()
            t_numbers.remove(now_number)

            history = func(t_numbers, adding_str, history)
            if (adding_str == '' and now_number == '0'):
                pass
            else:
                history = func(t_numbers, adding_str + now_number, history)

    return history

def solution(numbers):
    return len(func(list(numbers)))