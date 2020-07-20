import sys
num3 = int(sys.stdin.readline().strip())
i = range(0,num3)
for num3 in i:
    num,num2 = map(int,sys.stdin.readline().strip().split())
    print(num + num2)
