def compute_min_number_of_refills_naive(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.insert(0, 0)
    # stops.insert(len(stops), d)
    num_refills = 0
    current_refill = 0
    n = len(stops) - 1
    if d - stops[-1] > m:
        return -1
    if d <= m:
        return 0
    for i in range(len(stops) - 1):
        if stops[i + 1] - stops[i] <= m:
            num_refills += 1
        if stops[i + 1] - stops[i] > m:
            return -1

    return num_refills