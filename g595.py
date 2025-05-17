while True:
    try:
        n=int(input())
        long=0
        lt=[int(x) for x in input().split()]
        for i in range(len(lt)):
            if i==0 and lt[i]==0:
                long+=lt[i+1]
            elif i==(len(lt)-1) and lt[len(lt)-1]==0:
                long+=lt[len(lt)-2]
            else:
                if lt[i]==0:
                    long+=min(lt[i-1],lt[i+1])
        print(long)
    except:break