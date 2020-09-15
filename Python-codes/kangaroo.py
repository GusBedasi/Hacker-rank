def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 < v1:
        while x1 != x2:
            x1 += v1
            x2 += v2
            if x1 > x2:
                result = "NO"
                break
            else:
                result = "YES"
        print(result)
    else:
        print("NO")

kangaroo(0,3,4,2)
kangaroo(0,2,5,3)
kangaroo(21,6,47,3)