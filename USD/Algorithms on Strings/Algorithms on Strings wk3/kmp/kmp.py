# python3
import sys


def prefix_function(pattern):
    s = [0]
    border = 0

    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = s[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        s.append(border)
    return s


def find_pattern(pattern, text):
    result = []
    s = pattern + '$' + text
    S = prefix_function(s)
    for i in range(len(pattern) + 1, len(S)):
        if S[i] == len(pattern):
            result.append(i - 2 * len(pattern))
    return result


# f = open("./sample_tests/sample2")
# pattern = f.readline().strip()
# text = f.readline().strip()
# print(find_pattern(pattern, text))
if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))
