date_1=input("please input the date 1 in numbers: ")
ds1=date_1.split()
date_2=input("please input the date 2 in numbers: ")
ds2=date_2.split()

m1=int(ds1[1])
m2=int(ds2[1])
d1=int(ds1[0])
d2=int(ds2[0])
#monthsbig=[10,11]
#if i == m1 and i in monthsbig:
days=0
for i in range(m1,m2+1):
    if i == m1:
        days += (30-d1)
    elif i == m2:
        days += d2
    else :
        days += 30

print(days)

