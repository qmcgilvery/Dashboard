# python3


def parent(i):
    return i//2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def sift_down(i, data, size, swaps):
    max_index = i
    left = left_child(i)
    right = right_child(i)

    if left > size:
        return
    if left <= size and data[left] < data[max_index]:
        max_index = left
    if right <= size and data[right] < data[max_index]:
        max_index = right
    if max_index != i:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(max_index, data, size, swaps)


def build_heap(data):
    swaps = []
    size = len(data) - 1
    for i in range(len(data)//2, -1, -1):
        sift_down(i, data, size, swaps)
    return data

    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps


print(build_heap([5, 4, 3, 2, 1]))


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
