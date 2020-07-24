import sys
 
before = input()
now = before
cycle = 0
 
while True:
    cycle += 1
    if(len(now) == 1):
        now = '0' + now
        before = now
    now = now[-1] + (str(int(now[0]) + int(now[1])))[-1]
    if(now == before):
        print(cycle)
        break