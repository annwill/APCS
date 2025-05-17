while True :
    try:
        y1=y2=0
        best=-10000000
        a1,b1,c1=map(int, input().split())
        a2,b2,c2=map(int, input().split())
        n=int(input())
        for i in range(n+1):
            y1=a1*i*i+b1*i+c1
            y2=a2*(n-i)*(n-i)+b2*(n-i)+c2
            best=max(best,y1+y2)

        print(best)
    except :break    