def compareTriplets(a, b):
    a = a[:3]
    b = b[:3]

    aliceScore = 0
    bobScore = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            aliceScore += 1
        elif a[i] < b[i]:
            bobScore += 1
    
    return aliceScore, bobScore

compareTriplets([5, 6, 7], [3, 6, 10])
compareTriplets([17, 28, 30], [99, 16, 8])
compareTriplets([99, 16, 8], [17, 28, 30])
compareTriplets([100, 100, 100], [100, 100, 100])