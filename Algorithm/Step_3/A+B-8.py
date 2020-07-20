num3 = int(input())
i = range(0,num3)
for num3 in i:
    num,num2 = map(int,input().split())
    c = f"Case #{num3+1}:"
    v = f"{num} + {num2} ="
    print(c,v,num + num2)
