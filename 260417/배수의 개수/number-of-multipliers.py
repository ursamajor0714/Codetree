Q = [int(input()) for _ in range(10)]

res1=0
res2=0

for i in Q:
    if i%3==0:
        res1+=1
    if i%5==0:
        res2+=1
print(res1,res2)