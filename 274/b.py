def count_multiple_of_B(N, B, K, c):
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(B)] for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            for k in range(B):
                dp[i][j][k] = dp[i-1][j][k]
                if c[j-1] <= k:
                    dp[i][j][k] += dp[i-1][j-1][(k-c[j-1]+B)%B]
                dp[i][j][k] %= MOD
    return dp[N][K][0]

N, B, K = map(int, input().split())
c = list(map(int, input().split()))
print(count_multiple_of_B(N, B, K, c))
