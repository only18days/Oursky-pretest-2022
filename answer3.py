def NoRecur(n, cur):
    for i in range(n, 2, -1):
        cur = cur +1/(i*(i-1))
    return 1/2 + cur
       
