A, B, C = map(int, input().split())

if A==B==C:
    print(10000+A*1000)
elif A==B:
        print(1000+A*100)
elif B==C:
        print(1000+B*100)
elif C==A: 
        print(1000+C*100)

else:
    if B<C:
        B=C
    if A<B:
        A=B
    print(A*100)