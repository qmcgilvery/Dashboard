# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def pp(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    l = [0] * n
    l[1] = 1
    i = 0
    for i in range(2, n):
        l[i] = (l[i - 1] % 10) + (l[i - 2] % 10)
    last_num = l[i] + l[i - 1] % 10

    return last_num % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n
    piper = pp(10)
    pip = (n + 1) % piper
    pyp = piper + pip
    l = [0] * pyp
    l[1] = 1
    i = 0

    for i in range(2, pyp):
        l[i] = (l[i - 1]) + (l[i - 2])
    return sum(l) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    if to_index == 0:
        return 0
    if to_index == 1:
        return 1

    new_to_index = to_index % 60
    new_from_index = from_index % 60
    fibonacci_numbers = [0] * 120
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1

    if new_from_index > new_to_index:
        for i in range(2, 120):
            fibonacci_numbers[i] = (fibonacci_numbers[i - 2]) % 10 + (fibonacci_numbers[i - 1]) % 10
        return sum(fibonacci_numbers[new_from_index:60]) % 10 + sum(fibonacci_numbers[0:new_to_index + 1]) % 10
    for i in range(2, 60):
        fibonacci_numbers[i] = (fibonacci_numbers[i - 2]) % 10 + (fibonacci_numbers[i - 1]) % 10
    return sum(fibonacci_numbers[new_from_index:new_to_index + 1]) % 10

if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))

# print(last_digit_of_the_sum_of_fibonacci_numbers_again(5618252, 6583591534156))
# print(last_digit_of_the_sum_of_fibonacci_numbers_again(3, 7))
# print(5618252 % 60, 6583591534156 % 60)