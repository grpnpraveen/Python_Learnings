class x:
    print("test")
    name=''
    def __init__(self,x): 
        self.name=x
        print(":} started")
         
    def r(self):
        print("ok in middel")
    
    
    def __del__(self):
        print(":( ended")

class x2(x):                #it's constructor is include in class c
    print("test2")
    def p(self,g):
        self.name=g



c=x("name")

