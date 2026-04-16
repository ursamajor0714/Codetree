N=int(input())
Good=list(map(int, input().split()))

res=[x**2 for x in Good]
print(*res)