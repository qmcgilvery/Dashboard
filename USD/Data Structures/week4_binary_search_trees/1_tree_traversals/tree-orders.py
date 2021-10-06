# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

# sys = open("tests/01")


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.in_order = []
        self.pre_order = []
        self.post_order = []
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, ind):

        if ind == -1:
            return
        key = self.key[ind]
        left_child = self.key[self.left[ind]]
        if self.left[ind] != -1 and left_child >= key:
            self.in_order.append("x")
        left = self.left[ind]
        right = self.right[ind]
        self.inOrder(left)
        self.in_order.append(key)
        self.inOrder(right)

        return self.in_order

    def preOrder(self, ind):

        if ind == -1:
            return
        key = self.key[ind]
        left = self.left[ind]
        right = self.right[ind]
        self.pre_order.append(key)
        self.preOrder(left)
        self.preOrder(right)

        return self.pre_order

    def postOrder(self, ind):

        if ind == -1:
            return
        key = self.key[ind]
        left = self.left[ind]
        right = self.right[ind]
        self.postOrder(left)
        self.postOrder(right)
        self.post_order.append(key)

        return self.post_order


tree = TreeOrders()
tree.read()
print(" ".join(str(x) for x in tree.inOrder(0)))
# print(" ".join(str(x) for x in tree.preOrder(0)))
# print(" ".join(str(x) for x in tree.postOrder(0)))

# def main():
#     tree = TreeOrders()
#     tree.read()
#     print(" ".join(str(x) for x in tree.inOrder(0)))
#     print(" ".join(str(x) for x in tree.preOrder(0)))
#     print(" ".join(str(x) for x in tree.postOrder(0)))
#
#
# threading.Thread(target=main).start()
