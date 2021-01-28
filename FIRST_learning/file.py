fhand=input("Enter the name of the file:")
name=fhand+".txt"
x=open(name,'w')
z=input("Enter the data:")
y=x.writelines(z)
x=open(name)
for i in x:
    words=i.split()
print(words)

f=dict()
for word in words:
    f[word]=f.get(word,0)+1
print(f)
j=f.items()

d=list()
for h,u in j:
    d.append((u,h))
    d=sorted(d,reverse=True)
print(d)
