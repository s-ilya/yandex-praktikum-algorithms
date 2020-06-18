if __name__ == '__main__':
    universityIds = list(map(int, input().split(" ")))
    resultCount = int(input())

    universityIdFrequencies = dict()
    for universityId in universityIds:
        if universityId in universityIdFrequencies:
            universityIdFrequencies[universityId] += 1
        else:
            universityIdFrequencies[universityId] = 0

    idsSortedByFrequency = sorted(universityIdFrequencies.keys(),
                                  key=lambda key: universityIdFrequencies[key],
                                  reverse=True)

    print(" ".join(map(str, idsSortedByFrequency[:resultCount])))
