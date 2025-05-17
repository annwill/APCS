while True:
    try:
        a,b,c=map(int, input().split())
        if c==0:
            if a==0 and b==0:
                print(f'AND\nOR\nXOR')
            elif (a!=0 and b==0) or (a==0 and b!=0):
                print(f'AND')
            elif a!=0 and b!=0:
                print(f'XOR') 
        elif c==1:
            if (a!=0 and b==0) or (a==0 and b!=0):
                print(f'OR\nXOR')
            elif a!=0 and b!=0:
                print(f'AND\nOR') 
            elif a==0 and b==0:
                print('IMPOSSIBLE')       
    except :break