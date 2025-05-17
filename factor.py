n=int(input())
i,ans=1,0
# while i*i<n:
#     if n%i==0:
#         ans+=i+n//i
#         print(f'i= {i},ans={ans}')
#     i+=1
# print(f'i= {i}')
# if i*i==n:ans+=1

while i<=n:
    if n%i==0:
        ans+=i
    i+=1    
print(ans)        