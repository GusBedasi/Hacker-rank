def diagonalDifference(arr):
    # Write your code here
    
    rightToLeft = []
    leftToRight = []

    for i in range(len(arr)):
        leftToRight.append(arr[i][i])
        #print(arr[i][i])

    counter = len(arr) -1 # === 2 
    for i in range(len(arr)):
        rightToLeft.append(arr[i][counter])
        counter -= 1

    result = abs(sum(rightToLeft) - sum(leftToRight))

    #print(leftToRight, " = ", sum(leftToRight))
    #print(rightToLeft, " = ", sum(rightToLeft))
    #print(sum(leftToRight), " - ", sum(rightToLeft), " = ", result)
    #print("")

diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]])
diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])
