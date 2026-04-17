A,B = map(int, input().split())

Q=[A]

while A < B:
    if A%2 == 0:
        A+=3
    elif A%2 !=0:
        A*=2     
    if A > B:
        break
    Q.append(A)

print(*Q)