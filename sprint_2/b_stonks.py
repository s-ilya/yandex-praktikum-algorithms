def max_income(stonks):
    bying_mode = 'bying'
    selling_mode = 'selling'

    account = 0
    mode = bying_mode

    for today_index in range(len(stonks)):
        today_value = stonks[today_index]

        tomorrow_index = today_index + 1
        tomorrow_value = stonks[tomorrow_index] if tomorrow_index < len(stonks) else -1

        if mode == bying_mode and tomorrow_value > today_value:
            account -= today_value
            mode = selling_mode
        elif mode == selling_mode and today_value > tomorrow_value:
            account += today_value
            mode = bying_mode

    return account


if __name__ == '__main__':
    _ = int(input())

    print(max_income([
        int(price) for price in input().split(' ')
    ]))
