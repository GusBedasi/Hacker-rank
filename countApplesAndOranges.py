def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_counter = 0
    orange_counter = 0
    
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            apple_counter += 1

    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            orange_counter += 1
    
    print(apple_counter)
    print(orange_counter)

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
countApplesAndOranges(2,3,1,5,[-2],[-1])