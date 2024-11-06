k = []
for _ in range(9):
    i = int(input())
    k.append(i)
print(max(k))
print(k.index(max(k))+1)