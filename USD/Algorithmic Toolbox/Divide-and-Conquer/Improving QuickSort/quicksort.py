# python3

from random import randint


def partition3(array, left, right):

    x = array[left]
    j = left
    m = right
    i = j
    while i <= m:
        if array[i] < x:
            array[j], array[i] = array[i], array[j]
            j += 1
        elif array[i] > x:
            array[m], array[i] = array[i], array[m]
            m -= 1
            i -= 1
        i += 1
    return j, m


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     randomized_quick_sort(elements, 0, len(elements) - 1)
#     print(*elements)
#
arr = [3, 5, 6, 2, 7, 6, 8, 7, 2, 10]
randomized_quick_sort(arr, 0, len(arr) - 1)
print(arr)

