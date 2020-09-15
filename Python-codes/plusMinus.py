def plusMinus(arr):
    arr = arr[:100]

    counterPositive = 0
    counterNegative = 0
    CounterNull = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            counterPositive += 1
        elif arr[i] < 0:
            counterNegative += 1
        else:
            CounterNull += 1

    print(round(counterPositive / len(arr), 6))
    print(round(counterNegative / len(arr), 6))
    print(round(CounterNull / len(arr), 6))
    print("")

plusMinus([1, 1, 0, -1, -1])
plusMinus([-4, 3, -9, 0, 4, 1])