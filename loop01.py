n=[int(x) for x in input().split()]
# n=[5,7,-3,1,7,4,5,1,-3,2]
for i in range(3):
    x=int(input())
    if x in n:
        print(n.index(x))
    else:
        print('no')