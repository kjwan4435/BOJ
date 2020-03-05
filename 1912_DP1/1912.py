num = int(input())
arr = list(map(int,input().split()))
dp=[arr[0]]
for i in range(1,num): dp.append(dp[i-1]+arr[i]) if (dp[i-1]+arr[i]>arr[i]) else dp.append(arr[i])
print(max(dp))