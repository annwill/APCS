while True:
    try:
         x,y,z=map(int,input().split())
         c=max(x,y,z)
         a=min(x,y,z)
         b=x+y+z-(a+c)
         if a+b<=c:
            print(f'{a} {b} {c}\n No')
         elif a*a+b*b < c*c:
            print(f'{a} {b} {c}\n Obtuse')
         elif a**2+b**2>c**2:
            print(f'{a} {b} {c}\n Acute')
         elif a**2+b**2==c**2:
            print(f'{a} {b} {c}\n Right')
    except:break

   



