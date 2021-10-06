# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


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


# if __name__ == '__main__':
#     input_n = int(input())
#     print(last_digit_of_fibonacci_number(input_n))

print(last_digit_of_fibonacci_number(0, 7))