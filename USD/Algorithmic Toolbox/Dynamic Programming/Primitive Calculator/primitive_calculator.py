# python3
import sys


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    ops = {0: {0: 0, 0: 0}, 1: {0: 0, 1: '1 '}, 2: {0: 1, 1: '1 2 '}, 3: {0: 1, 1: '1 3 '}}
    if n < 4:
        return str(ops[n][0]).strip('()'), str(ops[n][1]).strip('()')
    for i in range(4, n + 1):
        pre = {0: ops[i - 1][0] + 1, 1: ops[i - 1][1]}
        if i % 3 == 0:
            if pre[0] < ops[i / 3][0] + 1:
                ops[i] = {0: pre[0], 1: pre[1] + str(1) + ' '}
            else:
                ops[i] = {0: ops[i / 3][0] + 1, 1: ops[i / 3][1] + str(i) + ' '}
        elif i % 2 == 0:
            if pre[0] < ops[i / 2][0] + 1:
                ops[i] = {0: pre[0], 1: pre[1] + str(i) + ' '}
            else:
                ops[i] = {0: ops[i / 2][0] + 1, 1: ops[i / 2][1] + str(i) + ' '}
        else:
            ops[i] = {0: pre[0], 1: pre[1] + str(i) + ' '}

    num_ops = str(ops[i][0].strip('()'))
    op_step = str(ops[i][1].strip('()'))

    return num_ops, op_step


print(compute_operations(10))

# if __name__ == '__main__':
#     input_n = int(input())
#     output_sequence = compute_operations(input_n)
#     print(len(output_sequence) - 1)
#     print(*output_sequence)

# input = sys.stdin.read()
# n = int(input)
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')

