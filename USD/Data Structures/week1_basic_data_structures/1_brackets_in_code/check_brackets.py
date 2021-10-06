# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(text[i])
            index.append(i + 1)
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            else:
                top = text[i]
                if are_matching(opening_brackets_stack[-1], text[i]):
                    opening_brackets_stack.pop()
                    index.pop()
                else:
                    return i + 1
                pass

    if opening_brackets_stack:
        return index[0]
    else:
        return "Success"


# print(find_mismatch("[](()"))


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
