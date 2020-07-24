num = int(input())
num6 = num
check_num = 1
while True:
    if check_num != 0:
        num1 = num6
        num2 = int(num1/10)
        num3 = num1 % 10
        num4 = num2 + num3
        num6 = (num3*10) + num4
        check_num += 1
    if num6 == num:
        print(check_num)
        break