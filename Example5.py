lis=[1,2,3,4,5]
for i in lis:
    print(i*i*i)

lis=[1,2,3,4,5,6,7,8,9,10]
s=list(filter(lambda x: x%2==1,lis))
print(s)