# python3
import sys


def BWT(text):
    bwt = []
    tt = text * 2
    k = [tt[i: i + len(text)] for i in range(len(text))]
    k.sort()
    for bw_matrix in k:
        bwt.append(bw_matrix[len(bw_matrix) - 1])
    return bwt


if __name__ == '__main__':
    # f = open("./sample_tests/sample2")
    # text = f.readline().strip()
    text = sys.stdin.readline().strip()
    print(*"".join(BWT(text)).split())