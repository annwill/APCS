while True:
    try:
        even=0
        odd=0
        s=input()
        s='0'+s[::-1]
        for i in range(1,len(s)):
             if (i+1)%2==0:
                 odd+=int(s[i])
             else:
                 even+=int(s[i] )   
        print(f'e ={even}')
        print(f'o={odd}')
        print(abs(odd-even))




    except:break     