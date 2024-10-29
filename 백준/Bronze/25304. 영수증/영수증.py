price = int(input())
sum = 0
N = int(input())
for i in range(1, N+1):
    a, b = map(int, input().split())
    sum = sum + a*b
if sum == price:
    print("Yes")
else:
    print("No")