def max_kids_with_cookies(kids: list, cookies: list):
    got_cookies = 0

    sorted_kids = sorted(kids, reverse=True)
    sorted_cookies = sorted(cookies, reverse=True)
    cookie_index = 0

    for kid_appetite in sorted_kids:
        if cookie_index == len(sorted_cookies):
            return got_cookies

        if kid_appetite <= sorted_cookies[cookie_index]:
            got_cookies += 1
            cookie_index += 1

    return got_cookies


if __name__ == '__main__':
    kids_n = int(input())
    kids = [
        int(kid) for kid in input().split(' ')
    ] if kids_n > 0 else []

    cookies_n = int(input())
    cookies = [
        int(cookie) for cookie in input().split(' ')
    ] if cookies_n > 0 else []

    print(max_kids_with_cookies(
        kids=kids, cookies=cookies
    ))
