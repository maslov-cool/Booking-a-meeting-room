n = int(input())
A = []
for i in range(n):
    l, r = [float(i) for i in input().split()]
    A.append([l, r])
B = []
while A:
    i = A.index(min(A, key=lambda x: (x[1], -x[0])))
    B.append(A[i])
    del A[i]
    j = 0
    while j != len(A):
        if B[-1][1] >= A[j][0]:
            del A[j]
        else:
            j += 1
print(len(B))
