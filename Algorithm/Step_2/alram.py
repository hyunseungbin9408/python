num1,num2 = map(int,input().split())
A = num2 - 45
if A >= 0 :
    print(num1,A)
elif A <= 0 and 24 > num1 != 0:
    print((num1-1),(A + 60))
elif A <= 0 and 24 > num1 == 0:
    print((num1+24-1),(A + 60))
