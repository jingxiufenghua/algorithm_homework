import pandas as pd
import numpy as np

a = "XYXZYXY"
b = "XZYZZYX"

#采用动态规划的方法
def maxsub(list_a,list_b):
    if not list_a or not list_b:
        return 0
    n_a = len(list_a)+1
    n_b = len(list_b)+1
    dp = [[0] * n_a for _ in range(n_b)]
    p =  [[0] * n_a for _ in range(n_b)]   # 1 代表左边，2代表左上，3代表上边, 0 代表最左边和最上边的初始值
    out_list = []

    for i in range(1,len(list_a)+1):
        for j in range(1,len(list_b)+1):
            temp_a = list_a[i-1]
            temp_b = list_b[j-1]
            if list_a[i-1] == list_b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                p[i][j] = 2    # 如果相等就记为2代表左上
            elif dp[i-1][j]>dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                p[i][j] = 3    # 不相等 上边的大 取上边的
            else:
                dp[i][j] = dp[i][j-1]
                p[i][j] = 1    # 不相等 左边的大 取左边的
    u,t = len(list_a),len(list_b)
    while u or t:
        if p[u][t]==2:
            out_list.append(list_a[u-1])
            u -= 1
            t -= 1
        elif p[u][t]==1:
            t -=1
        elif p[u][t]==3:
            u -=1
    return dp, p, out_list

dp,p,out_list = maxsub(a,b)
print(dp,"\n",p,"\n",out_list)