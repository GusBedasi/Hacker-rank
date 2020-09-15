def countingValleys(n, s):     
    sea_level = counter_valley = 0

    d = {'U':1, 'D':-1}
    for step in s:
        sea_level += d[step]
        if sea_level == 0 and step == 'U':
            counter_valley += 1

    return counter_valley

countingValleys(8, ["U","D","D","D","U","D","U","U"])
countingValleys(8, ["D","D","U","U","U","U","D","D"])