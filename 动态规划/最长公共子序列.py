def longest_char(text1:str, text2:str):
    n = len(text1)
    m = len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]  # 初始化计算矩阵
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

def longest_char_v1(text1:str, text2:str):
    n, m = len(text1), len(text2)
    dp = [0] * (n+1)
    for i in range(1, m+1):
        prev = dp[0]
        for j in range(1, n+1):
            tmp = dp[j]
            if text1[j-1] == text2[i-1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j-1], tmp)
            prev = tmp
    return dp[-1]
    

if __name__ == '__main__':
    text1 = '13456778'
    text2 = '357486782'
    print(longest_char_v1(text1, text2))
    