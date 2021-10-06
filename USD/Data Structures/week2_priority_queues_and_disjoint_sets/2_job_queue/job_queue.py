# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def parent(i):
    return i // 2


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
        swaps.append((max_index, i))
        sift_down(max_index, data, size, swaps)


def sift_up(i, data):
    while i > 0 and data[parent(i)] > data[i]:
        data[i], data[parent(i)] = data[parent(i)], data[i]
        i = parent(i)


def build_heap(data):
    swaps = []
    size = len(data) - 1
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, size, swaps)
    return data


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [[0] * 2 for i in range(n_workers)]
    for i in range(len(next_free_time)):
        next_free_time[i][1] = i
    t = 0
    build_heap(next_free_time)
    while t < len(jobs):  # Run until jobs are done
        m = next_free_time[0][0]
        result.append(AssignedJob(next_free_time[0][1], m))
        next_free_time[0][0] = next_free_time[0][0] + jobs[t]
        sift_down(0, next_free_time, len(next_free_time) - 1, [])
        if t < len(jobs) - 1:
            t += 1
        else:
            return result
    return result
        # for x in range(len(next_free_time)):
        #     if next_free_time[x][0] - m == 0:
        #         result.append(AssignedJob(next_free_time[x][1], m))
        #         next_free_time[x][0] = next_free_time[x][0] + jobs[t]
        #         # sift_down(x, next_free_time, len(next_free_time) - 1, [])
        #         if t < len(jobs) - 1:
        #             t += 1
        #         else:
        #             return result
    # return result

#
# j = [1] * 20
# print(assign_jobs(4, j))

# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     result = []
#     next_free_time = [0] * n_workers
#     for job in jobs:
#         next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#         result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job
#
#     return result
#
#


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
