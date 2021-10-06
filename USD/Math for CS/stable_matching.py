def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Write your code here
        if currentHusband != None:
            # Now "he" proposes to "she".
            # Decide whether "she" accepts, and update the following fields
            if herPreferences.index(he) < herPreferences.index(currentHusband):
                manSpouse[he] = she
                womanSpouse[she] = he
                unmarriedMen.remove(he)
                unmarriedMen.append(currentHusband)
            if herPreferences.index(he) > herPreferences.index(currentHusband):
                nextManChoice[he] = nextManChoice[he] + 1
        else:
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice

    # Note that if you don't update the unmarriedMen list,
    # then this algorithm will run forever.
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse


# You might want to test your implementation on the following two tests:
# assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
# assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])

def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    if a == 0 or b == 0:
        return max(a, b)

    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d

    return 1


# print(gcd(10, 6))


def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    if a == b:
        return 1

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


# print(gcdf(10, 6))

def squares(n, m):
    a = n
    b = m
    if n == m:
        return 1
    while n > 0 and m > 0:
        if n > m:
            n = n % m
        else:
            m = m % n

    d = max(n, m)
    return (a / d) * (b / d)


# print(squares(2, 2))

def lcm(a, b):
    return a*b / gcd(a, b)


print(9*5 - 27)


