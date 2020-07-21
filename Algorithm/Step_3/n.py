x, y = map(int,input().split())
if 1 <= x and 1 < y <= 10000:
    list1 = list(map(int,input().split()))
    for num1 in list1:
        if num1 < y:
            print(num1, end=" ") 