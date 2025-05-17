while True:
    try:
        n,d=map(int, input().split())
        t1=t2=0
        cnt=0
        tal=0
        for i in range(n):
            f=[int(x) for x in input().split()]
            t1=max(f)
            t2=min(f)
            if t1-t2>=d:
                tal+=int(sum(f)/len(f))
                cnt+=1

        print(f'{cnt} {tal}')
    except:break