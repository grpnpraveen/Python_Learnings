import xml.etree.ElementTree as ET
c=list()
stuff=ET.parse("Library.xml")
all = stuff.findall('dict/dict/dict')
x=0
for entry in all:
    for child in entry:
        if x==0:
            print(child.text,end=" =>")
            x=1
        else:
            print(child.text)
            x=0

    break

    
