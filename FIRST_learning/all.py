def Name():
    name=input('Enter your name:')
    print('WELCOME',name)
def add(x,y):
    add=x+y
    return add
g=9
p=int(input("ENTER THE VALUE OF P:"))

Name()

i=0
while i==0:
    try:
        y=int(input('Enter an integer:'))
        break
    except:
        print("------------------------NEED TO ENTER INTEGER ONLY----------------------")

print(type(y))
print("Enter the two integers to add:")
while i==0:
    try:
        a=int(input())
        break
    except:
        print("------------------------NEED TO ENTER INTEGER ONLY----------------------")
while i==0:
    try:
        b=int(input())
        break
    except:
        print("------------------------NEED TO ENTER INTEGER ONLY----------------------")
z=add(a,b) + y+p
print('The sum of the vaues entered by you is',end=":")
print(z)
for i in [5,4,3,1]:
    print(i)
while (p>5):
    print("ook")
    p=p-3
print("huhooooo!!"+" "+"HEYYYYY!!")
