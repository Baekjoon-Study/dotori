num1 = int(input())
num2 = list(input())

r1 = num1 * int(num2[2])
r2 = num1 * int(num2[1])
r3 = num1 * int(num2[0])

print(r1)
print(r2)
print(r3)
print(r1 + r2*10 + r3*100)