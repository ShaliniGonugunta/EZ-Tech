n=int(input())
dis= int(input())
total = 240
rem =total - dis
count= 0
for i in range(1,n):
    val = i*5
    rem-=val
    if rem<0:
        break
    else :
        count+= 1
print(count)