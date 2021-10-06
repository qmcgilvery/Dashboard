# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = 0
    while money > 0:
        while money >= 10:
            coins += 1
            money -= 10
        while money >= 5:
            coins += 1
            money -= 5
        while money >= 1:
            coins += 1
            money -= 1

    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))


