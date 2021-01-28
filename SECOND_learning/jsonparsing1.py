
import json
data='''
                    {
                        "name":"praveen",
                        "phonenumber":"513135131","ohm":{
                            "type":"ok","poop":"pp"
                        }
                    }'''

info=json.loads(data)
print(info['name'])
print(info['ohm']['type'])


data2=''' [
                {"name":"praveen","age":"20"},{"name":"bublu","age":"8"}
]'''
info1=json.loads(data2)

for item in info1:
    print(item["name"])
    print(item["age"])
