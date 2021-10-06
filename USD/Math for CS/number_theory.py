# def gcd(a, b):
#     assert a >= 0 and b >= 0 and a + b > 0
#
#     while a > 0 and b > 0:
#         if a >= b:
#             a = a % b
#         else:
#             b = b % a
#     return max(a, b)

def diophantine(a, b, c):
    d, x, y = gcd(a, b)
    assert c % d == 0

    x *= c / d
    y *= c / d

    return x, y


def gcd(a, b):
    # assert a >= b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y


def divide(a, b, n):
    # assert n > 1 and a > 0 and gcd(a, n) == 1

    d, x, y = gcd(a, n)
    x = x % n
    x = (b*x) % n
    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
    return x


print(divide(3, 1, 4))
# print(-4 % 9)