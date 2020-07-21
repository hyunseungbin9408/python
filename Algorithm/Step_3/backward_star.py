num1 = int(input())
for num2 in range(1, num1+1):
    for num3 in range(num1-num2):
        print(" ", end="")
    for num3 in range(num2):
        print("*", end="")
    print()
