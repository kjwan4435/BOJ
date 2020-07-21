[n, m ,k] = [3,8,4]
[n2,m2,k2] = [10, 6, 5]
[n3,m3,k3] = [2,10,4]
[n4,m4,k4] = [50,150,20]

def rec(N, k, depth, strict):
    depth += 1
    if strict == depth: return 1
    return rec(N,k-1,depth,strict)+rec(N-k,min(N-k,k),depth,strict)

def solution(n, m, k):
    answer = -1
    if m%2 == 1 or n>m or k<m/n or n == 1: 
        answer = 0
        return answer
    else:
        halfM = int(m/2)
        halfN = int((n+1)/2)
        halfNT = n - halfN
        
        print(rec(halfM,k,0,halfN))

        return answer

print(solution(n,m,k))
print(solution(n2,m2,k2))
print(solution(n3,m3,k3))
print(solution(n4,m4,k4))