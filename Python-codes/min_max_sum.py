def miniMaxSum(arr):
    minN = min(arr)
    maxN = max(arr)

    result = [0, 0]

    for i in range(len(arr)):
        result[0] += arr[i]
        result[1] += arr[i]
    
    result[0] = result[0] - maxN
    result[1] = result[1] - minN

    print(result[0], result[1])

miniMaxSum([1,3,5,7,9])
miniMaxSum([1,2,3,4,5])