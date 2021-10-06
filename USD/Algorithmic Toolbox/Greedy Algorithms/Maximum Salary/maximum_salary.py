# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_greater_or_equal(a, b):
    a = str(a)
    b = str(b)
    first = a + b
    second = b + a
    if first >= second:
        return True


def largest_number(numbers):
    number = list(map(str, numbers))
    a = ''
    nums = sorted(number)
    while nums:
        mn = 0
        for n in nums:
            if is_greater_or_equal(n, mn):
                mn = n
        a = a + mn
        nums.remove(mn)
    return int(a)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

# print(largest_number([2, 21, 23, 211, 213, 231, 232]))

