# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def is_covered(point, segment):
    return segment.start <= point <= segment.end


def compute_optimal_points(segments):

    # segments.sort()
    points = []
    while segments:
        mi = min([s.end for s in segments])
        points.append(mi)
        segments = [x for x in segments if not is_covered(mi, x)]
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)

# print (compute_optimal_points([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]))
