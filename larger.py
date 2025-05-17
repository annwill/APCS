n=[m for m in input().split()]
max,b=0,''
for i in n:
    sum=0
    for j in range(len(i)):
        sum+=int(i[j])
        if sum>=max:
            max=sum
            b=i
print(b)
print(max)


