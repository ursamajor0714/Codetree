fru = ["apple", "banana", "grape", "blueberry", "orange"]
Q = input()
P=0
for i in fru:
    if Q in i[3] or Q in i[2] :
        print(i)
        P+=1
print(P)