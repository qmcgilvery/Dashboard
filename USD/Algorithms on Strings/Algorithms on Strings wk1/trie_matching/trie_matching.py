# python3
import sys
import timeit
from timeit import Timer

NA = -1


class Node(object):
    def __init__(self):
        self.next = [NA] * 4

    def build_trie(self, patterns):
        tree = {}
        count = 0
        for pattern in patterns:
            current_node = 0
            for i in range(len(pattern)):
                current_symbol = pattern[i]
                if i == len(pattern) - 1:
                    end = 'end'
                    # ending = True
                else:
                    count += 1
                    end = count
                    # ending = False
                if current_node in tree and current_symbol in tree[current_node]:
                    if i == len(pattern) - 1:
                        tree[current_node].update({current_symbol:end})
                    if tree[current_node][current_symbol] == 'end':
                        break
                    if tree[current_node][current_symbol] != 'end':
                        current_node = tree[current_node][current_symbol]
                else:
                    new_node = {current_symbol: end}
                    # if current_node in tree and current_symbol not in tree[current_node]:
                    #     current_node = count
                    #     tree[current_node] = {}
                    #     tree[current_node].update(new_node)
                    if not current_node in tree:
                        tree[current_node] = {}
                        tree[current_node].update(new_node)
                    else:
                        tree[current_node].update(new_node)
                    current_node = count
        return tree

    def prefix(self, text, patterns, result, z, p):
        i = 0
        x = 0
        p += 1
        for _ in range(len(patterns)):
            p += 1
            s = text[x]
            if s in patterns[i]:
                if patterns[i][s] == 'end':
                    result.append(z)
                    return result
                if x >= len(text) - 1:
                    return
                elif text[x + 1] in patterns[patterns[i][s]]:
                    i = patterns[i][s]
                    x += 1
                else:
                    return
            else:
                return result

    def trie_matching(self, text, trie, result):
        z = 0
        p = 0

        tree = self.build_trie(trie)
        for _ in range(len(text)):
            self.prefix(text, tree, result, z, p)
            z += 1
            p += 1
            text = text[1:]
        return result


f = open("./sample_tests/sample1")
text = f.readline().strip()
n = int(f.readline().strip())
patterns = []
for i in range(n):
    patterns += [f.readline().strip()]

# text = sys.stdin.readline().strip()
# n = int(sys.stdin.readline().strip())
# patterns = []
# for i in range(n):
#     patterns += [sys.stdin.readline().strip()]

for i in range(len(patterns)):
    if len(patterns[i]) > len(text):
        patterns.pop(i)
mp = min([len(x) for x in patterns])

N = Node()
print(*N.trie_matching(text, patterns, []))

# ans = solve (text, n, patterns)
# sys.stdout.write (' '.join (map (str, ans)) + '\n')

# t = Timer(lambda: trie_matching(text, patterns, []))
# print(t.timeit(number=1))
