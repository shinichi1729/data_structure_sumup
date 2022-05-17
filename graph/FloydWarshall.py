INF = sys.maxsize
def warshall(V, edges):
    dp = [[INF]*V for _ in range(V)]
    for v in range(V):
        dp[v][v] = 0
    for s, t, c in edges:
        dp[s][t] = c

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dp[i][k] != INF and dp[k][j] != INF:
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    # 負閉路を含む <=> dp[i][i] < 0 となるiが存在
    negative_cycle = False
    for v in range(V):
        if dp[v][v] < 0:
            negative_cycle = True
    return dp, negative_cycle
