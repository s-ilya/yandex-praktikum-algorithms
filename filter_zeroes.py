if __name__ == '__main__':
    _ = input()
    points = list(
        filter(
            lambda point: point != 0,
            map(int, input().split(" "))
        )
    )

    print(" ".join(
        map(str, points)
    ))
