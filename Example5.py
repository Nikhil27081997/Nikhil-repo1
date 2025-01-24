lis=[1,2,3,4,5]
for i in lis:
    print(i*i*i)

lis=[1,2,3,4,5,6,7,8,9,10]
s=list(filter(lambda x: x%2==0,lis))
print(s)

lis=[10,20,30,40,50]
x=list(map(lambda x:x*2,lis))
print(x)


from functools import reduce #pkg/library
lis=[10,20,30,40,50]
x=reduce (lambda x,y:x+y, lis)
print(x)
