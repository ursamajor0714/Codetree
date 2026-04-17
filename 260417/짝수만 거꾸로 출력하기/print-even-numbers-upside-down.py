N = int(input())
Hap = list(map(int, input().split()))
hap = []

for i in Hap:
    if i%2 == 0 :
        hap.append(i)

print(*hap[::-1])