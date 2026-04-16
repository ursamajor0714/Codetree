A,B=list(input().split())

Q=list(A)
W=list(B)

if len(Q) == len(W) :
    print("same")
elif len(Q) > len(W):
    print(f"{''.join(Q)} {len(Q)}")
else:
    print(f"{''.join(W)} {len(W)}")