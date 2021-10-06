# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        # def compute_height(self):
        #         # Replace this code with a faster implementation
        #         maxHeight = 0
        #         for vertex in range(self.n):
        #                 height = 0
        #                 i = vertex
        #                 while i != -1:
        #                         height += 1
        #                         i = self.parent[i]
        #                 maxHeight = max(maxHeight, height);
        #         return maxHeight;
        def compute_height(self):
                d = {}
                max_height = 0
                for vertex in range(self.n):
                        height = 0
                        current = vertex
                        c = ''
                        while c != -1:
                                height += 1
                                c = self[current]
                                if c == -1:
                                        d[vertex] = height
                                elif c in d:
                                        d[vertex] = height + d[c]
                                else:
                                        d[vertex] = height
                                current = self[current]
                maximum = max(d.values())
                return maximum

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
