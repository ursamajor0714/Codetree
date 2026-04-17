N = int(input())
target = N
current_sum = 0
i = 0

while current_sum < target:
    i += 1
    current_sum += i

print(f"{i}")