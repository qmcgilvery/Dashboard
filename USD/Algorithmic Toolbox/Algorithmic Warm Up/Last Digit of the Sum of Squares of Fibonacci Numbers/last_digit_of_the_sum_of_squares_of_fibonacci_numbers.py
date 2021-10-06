# python3
def pp(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


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

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

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
    return sum([f ** 2 for f in l]) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))

