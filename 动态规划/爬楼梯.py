def climbstairs(n:int)->int:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]


if __name__ == '__main__':
    print(climbstairs(6))