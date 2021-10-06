#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.in_order = []
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
        right_child = self.key[self.right[ind]]
        if self.left[ind] != -1 and left_child >= key:
            self.in_order.append("x")
        if self.right[ind] != -1 and right_child < key:
            self.in_order.append("x")
        left = self.left[ind]
        right = self.right[ind]
        self.inOrder(left)
        self.in_order.append(key)
        self.inOrder(right)

        return self.in_order

    def IsBinarySearchTree(self):
        if self.n <= 1:
            return True
        a = self.inOrder(0)
        if 'x' in a:
            return False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False

        return True


def main():
    tree = TreeOrders()
    tree.read()
    if tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
#
# def main():
#   nodes = int(sys.stdin.readline().strip())
#   tree = []
#   for i in range(nodes):
#     tree.append(list(map(int, sys.stdin.readline().strip().split())))
#   if IsBinarySearchTree(tree):
#     print("CORRECT")
#   else:
#     print("INCORRECT")
#
# threading.Thread(target=main).start()
