while True:
    try:
        n=int(input('輸入測資:'))
        for i in range(n):
            a,b,c,d=map(int,input('輸入四值').split())
            if (a+c==2*b):
                x=b-a
                print("%d %d %d %d %d" %(a,b,c,d,x+d))
            elif (a*c==b**2):
                x=b/a
                print("%d %d %d %d %d" %(a,b,c,d,x*d))
            print('現是 %d' %i)
    except:break

