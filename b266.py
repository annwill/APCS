while True:
    def turn(r,c,a):
        j=0
        b=[[0]*c for i in range(r)]
        for i in range(len(a)-1,-1,-1):
            b[j]=a[i]
            j+=1
        a=b    
        return(len(a),len(a[0]),a)   
     
    def roate(r,c,a):
        b=[[0]*r for i in range(c)]
        for i in range(c):
            for j in range(r):
                b[i][j]=a[j][c-1-i]
        a=b
        return (len(a),len(a[0]),a)
    try:
        r,c,m=map(int,input().split())
        a=[[0]*c for i in range(r)]
        for i in range(r):
            k=[int(x) for x in input().split()]
            for j in range(c):
                a[i][j]=k[j]
        km=[int(x) for x in input().split()]
        for kk in km[::-1]:
            if kk==1:
              r,c,a =turn(r,c,a)
            else:
              r,c,a= roate(r,c,a)

        print(f'{r} {c}')
        for i in range(r):
            for j in range(c):
                print(f'{a[i][j]} ',end='')
            print()
    except:break 
    
   