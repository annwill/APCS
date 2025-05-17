while True:
    try:
        n=int(input())        
        for i in range(n):
            s=''
            x1=[int(x) for x in input().split()]
            x2=[int(x) for x in input().split()]
            if x1[1]==x1[3] or x1[1]!=x1[5] or x2[1]==x2[3] or x2[1]!=x2[5] :
                s+='A'
            if x1[6]!=1 or x2[6]!=0:
               s+='B'
            if x1[1]==x2[1] or x1[3]==x2[3] or x1[5]==x2[5]:
                s+='C'
            if not s:
                print('None') 
            else:
                print(s)  
       
    except:break   
