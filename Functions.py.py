user_str=input('Enter string:')
l=user_str.split()
d={}
for i in l:
    d[i]=d.get(i, 0)+1
print(d)
        