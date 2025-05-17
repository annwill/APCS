tal,s=0, ''
for i in range(2):
 a=[int(x) for x in input().split()]
 s+=str(max(a))+' '
 tal+=max(a)
print(s+str(tal))
