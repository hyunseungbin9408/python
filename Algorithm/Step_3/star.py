num1 = int(input())
i = range(0, num1)
for num1 in i:
    for num2 in i:
        if num2 <= num1:
            print("*", end='')
    print()
