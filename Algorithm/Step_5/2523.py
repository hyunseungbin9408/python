num1 = int(input())
num3 = 0
num4 = 0
i = range(0, (num1*2-1))
for num1 in i:
    for num2 in i:
        if num3 <= num1:
            print("*", end='')
        num3 += 1    
    print()
