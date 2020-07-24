num = 1
num2 = 0
while True:
    try:
        if 0 < num and num2 < 10:
            num,num2 = map(int,input().split())
            print (num + num2)
    except: 
        break