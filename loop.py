# s='thexFFxg X ggXxb'
s='The kaoshUIng HIgh school'
# u=0
# l=0
# for x in s:
#     if x==x.upper():
#         u+=1
#     elif x==x.lower():
#         l+=1
# print(f'大寫字母 {u}')
# print(f'小寫定母 {l}')
ss=s.lower()
d={}
for i in ss:
    d[i]=ss.count(i)
print(d)
print(max(d.values()))
print(max(d,key=d.get))
# for k,v in d.items():
#     if v==max(d.values()):
#         print(k)
#         break

