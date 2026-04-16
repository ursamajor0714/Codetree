a,b=map(int, input().split())

juapanda=[a, b]

for _ in range(8):
    juapanda.append((juapanda[-1]+juapanda[-2]) % 10)

print(*juapanda)

