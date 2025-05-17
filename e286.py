while True:
    try:
        acc=0
        ss=''
        for i in range(2):
            home=[int(x) for x in input().split()]
            away=[int(x) for x in input().split()]
            ss+=str(sum(home))+':'+str(sum(away))+'\n'
            if sum(home)>sum(away): acc+=1
        print(ss, end='')
        if acc>=2:
            print('Win') 
        elif acc==1:
            print('Tie')
        else:
            print('Lose')
    except:break    