def majority_element(elements):
    assert len(elements) <= 10 ** 5

    h = len(elements) / 2
    element1 = elements[:len(elements) // 2]
    element2 = elements[len(elements) // 2:]
    removed1 = 0
    removed2 = 0
    while len(element1) > len(elements[:len(elements) // 2]) / 2:
        if element1.count(element1[0]) >= len(element1) / 2 + removed1:
            if element1.count(element1[0]) + elements[len(elements) // 2:].count(element1[0]) > h:
                return 1
            else:
                removed1 = removed1 + element1.count(element1[0])
                element1 = list(filter(lambda a: a != element1[0], element1))
        else:
            removed1 = removed1 + element1.count(element1[0])
            element1 = list(filter(lambda a: a != element1[0], element1))
    while len(element2) > len(elements[len(elements) // 2:]) / 2:
        if element2.count(element2[0]) >= len(element2) / 2 + removed2:
            if element2.count(element2[0]) + elements[:len(elements) // 2].count(element2[0]) > h:
                return 1
            else:
                removed2 = removed2 + element2.count(element2[0])
                element2 = list(filter(lambda b: b != element2[0], element2))
        else:
            removed2 = removed2 + element2.count(element2[0])
            element2 = list(filter(lambda b: b != element2[0], element2))
    return 0