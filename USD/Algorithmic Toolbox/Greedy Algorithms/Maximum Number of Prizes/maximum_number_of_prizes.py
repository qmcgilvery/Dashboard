# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    a = n
    i = 1
    while i <= n:
        summands.append(i)
        n = n - i
        i = i + 1
    r = a - sum(summands)
    summands[-1] = summands[-1] + r

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

# print (compute_optimal_summands(100))
