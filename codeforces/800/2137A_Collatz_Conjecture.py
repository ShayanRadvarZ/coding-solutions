t= int(input())
ans = []
for i in range(t):
    k, x = map(int, input().split())
    ans.append(x << k)
print(*ans, sep="\n")
