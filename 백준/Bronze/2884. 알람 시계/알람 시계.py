H, M = map(int, input().split())

if  45 <= M <= 59:
    c = M - 45 
    print(H, c)
elif 0 <= M < 45:
    c = M - 45
    c = -c
    k = 60 - c
    h = H - 1
    if H == 0:
        h = 23
    print(h, k)
