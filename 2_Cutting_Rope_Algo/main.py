'''
Dynamic Programming ---

Design an algorithm which takes a positive interger representing a length of rope. This rope can be divided into any number of smaller integer lengths.
Return the maximum product you can get from multiplying the smaller lengths.
'''
def cutrope(n):
    dp = [None, 1]

    for m in range(2, n+1):
        j = m - 1
        i = 1
        max_product = 0
        while i <= j:
            max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
            j -= 1
            i += 1
        dp.append(max_product)
    return dp[n]

print(cutrope(3))
