N = int(input())
result = []

for score in range(N, 101):
    if score >= 90:
        result.append("A")
    elif score >= 80:
        result.append("B")
    elif score >= 70:
        result.append("C")
    elif score >= 60:
        result.append("D")
    else:
        result.append("F")

print(" ".join(result))