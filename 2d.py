# m,n =map(int, input().split())
# a=[]
# for i in range(m):
#     a.append([int(x) for x in input().split()])

# print(a)
# lst3=[]
# lst2=[[1,4],[2,5],[3,6]]
# print(lst2)
# for i in range(len(lst2)-1,-1,-1):
#     lst3.append(lst2[i])
# lst2=lst3
# print(lst2)
# a=[[4,8],[3,7],[2,6],[1,5]]
a=[[1,4],[2,5],[3,6]]
b=[[0]*3 for i in range(2)]
# print(b)

for i in range(2):
    id=len(a)
    for j in range(3):
        id-=1
        b[i][j]=a[id][i]
print(b)
