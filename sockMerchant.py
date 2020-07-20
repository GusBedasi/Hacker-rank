from collections import Counter

def sockMerchant(n, ar):
    pairCounter = 0
    if 1 <= n <= 100:
        for val in Counter(ar).values():
            pairCounter += val // 2
        print(Counter(ar).values())
        return pairCounter


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
#sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
