while True:
    def turn(r,c,a):
        j=0
        b=[[0]*c for i in range(r)]
        for i in range(len(a)-1,-1,-1):
            # print(a[i])
            b[j]=a[i]
            j+=1
        a=b    
        return(len(a),len(a[0]),a)   
     
    def roate(r,c,a):
        b=[[0]*r for i in range(c)]
        for i in range(c):
            id=len(a)
            for j in range(r):
                id-=1
                b[i][j]=a[id][i]
            
        a=b
        return (len(a),len(a[0]),a)
    try:
        r,c,m=map(int,input().split())
        a=[[0]*c for i in range(r)]
        for i in range(r):
            k=[int(x) for x in input().split()]
            # print(m)
            for j in range(c):
                a[i][j]=k[j]
        print(a)
        km=[int(x) for x in input().split()]
        for kk in km:
            if kk==1:
              r,c,a =turn(r,c,a)
              print(a)
              print(f'r={r}  c={c}')
            else:
              r,c,a= roate(r,c,a)
              print(a)
              print(f'r={r}  c={c}')
    except:break 
    
   