while True:
    try:
        a,b=map(int ,input().split())
        n=int(input())
        p1=0
        for i in range(n):
            c=[int(x) for x in input().split()]
            t1=t2=0
            for m in c:
                if m==a :t1+=m
                if m==-a:t1+=m
                if m==b :t2+=m
                if m==-b: t2+=m
            if t1>0 and t2>0 : p1+=1    
        # print(f't1={t1}')
        # print(f't2={t2}')
        print(p1)
    except:break    