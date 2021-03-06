# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    l = [0] * n
    l[1] = 1
    i = 0
    for i in range(2, n):
        l[i] = l[i - 1] + l[i - 2]

    return l[i] + l[i-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))



