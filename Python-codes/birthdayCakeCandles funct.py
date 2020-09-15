def birthdayCakeCandles(ar):
    taller = max(ar)
    counter = 0

    for i in range(len(ar)):
        if ar[i] == taller:
            counter += 1

    return counter

birthdayCakeCandles([4, 4, 1, 3])
birthdayCakeCandles([3, 2, 1, 3])